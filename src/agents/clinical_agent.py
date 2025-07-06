from src.agents.base_agents import BaseAgent
from src.core.config import CLINICAL_AGENT_MODEL
from src.utils.prompts import CLINICAL_AGENT_PROMPT

from src.tools.clinical_tools import searchWeb, ragTool


class ClinicalAgent(BaseAgent):
    def __init__(self) -> None:
        """Initializes the ClinicalAgent with the model and tools"""

        super().__init__(
            CLINICAL_AGENT_MODEL,
            [searchWeb, ragTool],
            CLINICAL_AGENT_PROMPT,
        )
