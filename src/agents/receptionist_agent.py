from src.agents.base_agents import BaseAgent
from src.core.config import RECEPTIONIST_AGENT_MODEL
from src.utils.prompts import RECEPTIONIST_AGENT_PROMPT

from src.tools.receptionist_tools import fetchPatientReport, callClinicalAgent


class ReceptionistAgent(BaseAgent):
    def __init__(self) -> None:
        """Initializes the ReceptionistAgent with the model and tools"""

        super().__init__(
            RECEPTIONIST_AGENT_MODEL,
            [fetchPatientReport, callClinicalAgent],
            RECEPTIONIST_AGENT_PROMPT,
        )
