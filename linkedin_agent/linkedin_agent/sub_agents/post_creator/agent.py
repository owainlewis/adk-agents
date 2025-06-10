from google.adk.agents import Agent

from . import prompt

from .. import model

post_creator = Agent(
    name="post_creator",
    description="Creates engaging LinkedIn posts based on structured briefs",
    model=model.MODEL,
    instruction=prompt.AGENT_PROMPT
)