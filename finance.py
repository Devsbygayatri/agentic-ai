from agno.agent import Agent
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

def build_Agent():
    return Agent(
        model=Gemini(id="gemini-3.6-flash"),
        tools=[[DuckDuckGoTools()],YFinanceTools(all=True)],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools whenever possible.Format your response using markdown and use tables to display data where possible."],
        debug_mode=True
    )

gemini_agent = build_Agent()

gemini_agent.print_response("Share the MSFT stock price and analyst recommendations")