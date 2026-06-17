from crewai import Agent

researcher = Agent(
    role="Researcher",
    goal="Learn CrewAI",
    backstory="An AI expert who helps users learn CrewAI.",
    verbose=True
)

print("Agent created successfully!")