from dotenv import load_dotenv
from src.ingetsor.DataIngestor import DataIngestor

load_dotenv()

data_ingestor = DataIngestor()
# data_ingestor.ingest_pdf(
#     "data/clinical-handbook-of-nephrology.pdf", "datasmith", "nephrology"
# )
data_ingestor.ingest_pdf("data/article_1.pdf", "datasmith", "nephrology")
