from pinecone import Pinecone
from src import constants
import os


class RAGQueryTool:
    def __init__(self):
        self.pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index = self.pc.Index(constants.PINECONE_INDEX_NAME)

    def query_database(self, query, namespace, top_k=3):
        """Database ko query karega and top_k results return karega"""

        query_embedding = self.pc.inference.embed(
            model=constants.PINECONE_EMBEDDING_MODEL,
            inputs=[query],
            parameters={"input_type": "query"},
        )

        intermediate_results = self.index.query(
            namespace=namespace,
            vector=query_embedding[0].values,
            top_k=top_k,
            include_values=False,
            include_metadata=True,
        )

        if not intermediate_results["matches"]:
            return "No relevant data found"

        reranked_results = self.pc.inference.rerank(
            model=constants.PINECONE_RERANKER_MODEL,
            query=query,
            documents=[
                match["metadata"]["text"] for match in intermediate_results["matches"]
            ],
            top_n=top_k,
            return_documents=True,
            parameters={"truncate": "END"},
        )

        retrieved_results = [item["document"]["text"] for item in reranked_results.data]

        retrieved_results_str = "---\n" + query + "\n"
        retrieved_results_str += "\n".join(retrieved_results)
        retrieved_results_str += "\n---\n"

        return retrieved_results_str


def rag_tool(
    query: str, namespace: str = constants.PINECONE_NAMESPACE, top_k: int = 3
) -> str:
    """RAG tool to query the database and return top_k results."""
    rag_query_tool = RAGQueryTool()
    return rag_query_tool.query_database(query, namespace, top_k)
