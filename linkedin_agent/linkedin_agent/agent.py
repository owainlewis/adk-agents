from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from dotenv import load_dotenv

from . import prompt
from .sub_agents.brief_extractor.agent import extract_brief

load_dotenv()

root_agent = LlmAgent(
    name="linkedin_content_strategist",
    model="gemini-2.5-flash-preview-05-20",
    instruction=prompt.AGENT_PROMPT,
    description="LinkedIn content strategist with specialized tools for viral content creation",
    tools=[AgentTool(agent=extract_brief)]
)