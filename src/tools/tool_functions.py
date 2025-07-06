from typing import Optional, Any, List, Dict
from datetime import datetime, timezone, timedelta

from langchain.tools.base import ToolException
from langchain_core.runnables import RunnableConfig

from langchain_community.tools import DuckDuckGoSearchResults


def fetch_patient_report(name: str) -> str:
    try:
        with open("data/patient_reports.json", "r") as file:
            data = file.read()
            reports = eval(data)  # Assuming the file contains a valid Python dictionary
            for report in reports:
                if report["patient_name"].lower() == name.lower():
                    return str(report)
        return f"No report found for patient: {name}"

    except FileNotFoundError:
        return "Patient reports file not found."
    except Exception as e:
        return f"An error occurred while fetching the report: {str(e)}"


def search_web(query: str) -> str:
    try:
        search = DuckDuckGoSearchResults(output_format="list", num_results=5)
        results = search.invoke(query)
        if not results:
            return "No search results found."
        return str(results)
    except Exception as e:
        return f"An error occurred while searching the web: {str(e)}"


def call_clinical_agent(
    query: str,
    patient_record_summary: Optional[str] = None,
    chat_history: Optional[List[Dict[str, Any]]] = None,
) -> str:
    try:
        from src.agents.clinical_agent import ClinicalAgent

        prompt = f"Patient Record Summary: {patient_record_summary}\n\nQuery: {query}"

        agent = ClinicalAgent()
        response = agent.invoke(
            user_input=prompt,
            chat_history=chat_history or [],
        )
        return response
    except Exception as e:
        return f"An error occurred while calling the clinical agent: {str(e)}"
