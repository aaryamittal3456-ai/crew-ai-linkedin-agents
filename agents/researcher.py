import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

researcher = Agent(
    role="LinkedIn Researcher",
    goal="Find valuable insights about a topic for LinkedIn content.",
    backstory="""
    You are an expert content researcher who finds
    interesting trends, statistics, and insights.
    """,
    llm=groq_llm,
    verbose=True
)