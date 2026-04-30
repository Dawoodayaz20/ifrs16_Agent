from agents import Agent, Runner, handoff
from financial_tools.finance_tools import get_all_leases
from agent_config import config

financial_assistant: Agent = Agent(
    name="Finance_Manager",
    instructions=f"""
    You are Finance_Manager, a smart and proactive personal finance agent. You have access to the user's financial data and can take actions through the tools provided to help them manage, analyze, and optimize their cashflow.
        """,
    tools=[get_all_leases],
    handoff_description=""" 
        Answer any query regarding user's personal finance and can take actions through the tools provided.
        It can fetch all leasing data.
        """
    )
# if __name__ == '__main__':
#   asyncio.run(kickoff(question1, userID, name, email))