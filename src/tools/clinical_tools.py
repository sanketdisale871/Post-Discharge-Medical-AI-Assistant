from langchain.tools import StructuredTool

from src.tools.tool_functions import search_web
from src.tools.rag_tool import rag_tool

from src.tools.schema import searchWebInput, ragToolInput


searchWeb = StructuredTool.from_function(
    name="search_web",
    description="Searches the web for information based on the provided query",
    args_schema=searchWebInput,
    func=search_web,
    handle_tool_error=True,
)

ragTool = StructuredTool.from_function(
    name="rag_tool",
    description="Retrieves relevant information from the database using RAG (Retrieval-Augmented Generation) technique given a query",
    args_schema=ragToolInput,
    func=rag_tool,
    handle_tool_error=True,
)
