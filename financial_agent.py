from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv()


websearch_agent = Agent(
    name="Web Search Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include the sources"],
    show_tools=True,
    markdown=True,
)

## financial agent 

finance_agent = Agent(
    name = "Finance Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools=True,
    markdown=True,

)


multi_agent = Agent(
    team=[websearch_agent, finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Use tables to display the data", "Always include the sources"],
    show_tools=True,
    markdown=True,
)

multi_agent.print_response("Summarise analys recommendations and share the latest news for NVDA",stream=True)
