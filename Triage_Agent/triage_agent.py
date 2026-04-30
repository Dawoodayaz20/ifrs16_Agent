from agents import Agent, Runner, function_tool, handoff, RunContextWrapper
from Finance_Agent.financial_agent import financial_assistant
from general_assistant.general_agent import general_assistant
from context import User_Context
from agent_config import config

async def handoff_financial_agent(ctx: RunContextWrapper[User_Context]):
    print(f"Financial agent called with Id:{ctx.companyId}")



async def kickoff(question: str, companyId: str, token: str):
    user_context = User_Context(
            companyId=companyId,
            token=token,
        )
    try:
        Triage_Agent: Agent = Agent[User_Context](
        name="Triage_Agent",
        instructions="""
            You are a silent triage agent. Do not respond to the user directly.        
            Route to "Finance_Manager" if the user asks about:
            - Their transactions, expenses, cashflow, or balance
            - Leases, payments, or financial data specific to them
            - Any action on their personal financial records
            
            Route to "General_Assistant" for everything else:
            - Greetings or small talk
            - General knowledge or accounting standards
            - App navigation or how-to questions
        """,
        handoffs=[financial_assistant, general_assistant]
        )
        
        result = await Runner.run(
            Triage_Agent,
            input=question,
            run_config=config,
            context=user_context,
        )
        print(result.final_output)
        return result.final_output

        
    except Exception as error:
        print(f"Exception occured! {error}")
        return {"Exception occured": error }

