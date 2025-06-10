from google.adk import Agent
from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06" 

extract_brief = Agent(
    name="brief_creator",
    description="Extracts structured briefs from content for LinkedIn posts",
    model=MODEL,
    instruction=prompt.AGENT_PROMPT
)
