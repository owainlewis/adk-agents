from google.adk import Agent
from . import prompt

from .. import model

extract_brief = Agent(
    name="brief_creator",
    description="Extracts structured briefs from content for LinkedIn posts",
    model=model.MODEL,
    instruction=prompt.AGENT_PROMPT
)
