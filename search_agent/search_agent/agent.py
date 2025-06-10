from google.adk.agents import Agent
from google.adk.tools import google_search

from dotenv import load_dotenv

load_dotenv()

MODEL= "gemini-2.5-flash-preview-05-20"

PROMPT = """
You are a helpful assistant that can search the web using Google Search to answer user questions.
"""

root_agent = Agent(
    name="search_assistant",
    model=MODEL,
    instruction=PROMPT,
    description="An assistant that can search the web.",
    tools=[google_search]
)