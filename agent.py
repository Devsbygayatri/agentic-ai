from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()
from agno.tools.duckduckgo import DuckDuckGoTools

def build_Agent():
    return Agent(
        model=Gemini(id="gemini-3.6-flash"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

gemini_agent = build_Agent()

gemini_agent.print_response("Is it safe to travel UAE today?")