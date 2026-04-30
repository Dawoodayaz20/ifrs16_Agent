from agents import Agent


general_assistant: Agent = Agent(
    name="General_Assistant",
    instructions=f"""
            You are a helpful general assistant.
            Answer greetings, general knowledge questions, accounting concepts, and app navigation queries.
            You do not have access to the user's financial data.
        """,
    handoff_description="Handles general queries, greetings, app navigation, and financial questions that are not personalized to user's data"
    )



