from crewai import Task

research_task = Task(
    description="""
    Research the latest trends in AI Agents and
    provide insights that would be valuable for a LinkedIn audience.
    """,
    expected_output="""
    A concise research report with key insights,
    trends, and actionable takeaways.
    """,
    agent=None  # Will be assigned in main.py
)