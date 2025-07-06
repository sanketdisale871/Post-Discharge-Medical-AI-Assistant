from langchain.tools import StructuredTool

from src.tools.tool_functions import fetch_patient_report, call_clinical_agent

from src.tools.schema import getPatientReportInput, callClinicalAgentInput


fetchPatientReport = StructuredTool.from_function(
    name="fetch_patient_report",
    description="Fetches the patient report given the patient's name",
    args_schema=getPatientReportInput,
    func=fetch_patient_report,
    handle_tool_error=True,
)

callClinicalAgent = StructuredTool.from_function(
    name="call_clinical_agent",
    description="Calls the Clinical Agent with a query and optional chat history",
    args_schema=callClinicalAgentInput,
    func=call_clinical_agent,
    handle_tool_error=True,
    return_direct=True,  # Return directly
)
