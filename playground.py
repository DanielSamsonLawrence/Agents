from phi.playground import Playground, serve_playground_app
from phi.agent import Agent
from phi.llm.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create agents
search_agent = Agent(
    name="Web Search Agent",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[DuckDuckGo()],
    instructions=["Always include the sources"],
    show_tools=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[YFinanceTools()],
    instructions=["Use tables to display financial data"],
    show_tools=True,
    markdown=True,
)

# Create and serve playground
if __name__ == "__main__":
    playground = Playground(
        agents=[search_agent, finance_agent],
        display_name="Financial Research Assistant",
        host="0.0.0.0",  # Allow external connections
        port=7777,       # Specify port
        api_base_url="http://localhost:7777"
    )
    serve_playground_app(playground,
                         host="0.0.0.0",
        port=7777)