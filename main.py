from crewai import Crew

from agents.researcher import researcher
from agents.strategist import strategist

from tasks.research_task import research_task
from tasks.strategy_task import strategy_task

# ✅ Assign agents to tasks
research_task.agent = researcher
strategy_task.agent = strategist

crew = Crew(
    agents=[researcher, strategist],
    tasks=[research_task, strategy_task],
    verbose=True
)

result = crew.kickoff()

print("\nFINAL OUTPUT:\n")
print(result)