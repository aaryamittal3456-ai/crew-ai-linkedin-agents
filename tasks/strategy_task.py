from crewai import Task
from agents.strategist import strategist

strategy_task = Task(
    description="""
    Create a LinkedIn content strategy based on the research.
    Include:
    - Hook
    - Main points
    - CTA
    """,
    expected_output="""
    A detailed content outline for a LinkedIn post.
    """,
    agent=strategist
)