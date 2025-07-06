from enum import Enum
from typing import Optional, Annotated
from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Any


class getPatientReportInput(BaseModel):
    name: Annotated[
        str, Field(description="Name of the patient to fetch the report for")
    ]


class searchWebInput(BaseModel):
    query: Annotated[
        str, Field(description="Search query to find information on the web")
    ]


class ragToolInput(BaseModel):
    query: Annotated[str, Field(description="Query to retrieve relevant information")]
    top_k: Annotated[int, Field(description="Number of top results to return")] = 3


class callClinicalAgentInput(BaseModel):
    query: Annotated[str, Field(description="Query to send to the clinical agent")]
    patient_record_summary: Annotated[
        str,
        Field(
            description="Summary of the patient's record to provide context for the query"
        ),
    ]
