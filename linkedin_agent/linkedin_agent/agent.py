from google.adk.agents import Agent
from dotenv import load_dotenv
from .tools import extract_brief

load_dotenv()

PROMPT = """
You are a LinkedIn content strategist with specialized tools for creating viral LinkedIn content.
"""

root_agent = Agent(
    name="linkedin_content_strategist",
    model="gemini-2.5-flash-preview-05-20",
    instruction=PROMPT,
    description="LinkedIn content strategist with specialized tools for viral content creation",
    tools=[extract_brief]
)