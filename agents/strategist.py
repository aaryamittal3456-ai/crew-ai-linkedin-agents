import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

strategist = Agent(
    role="LinkedIn Content Strategist",
    goal="Create a content strategy and outline from research findings.",
    backstory="""
    You are an expert LinkedIn content strategist.
    You transform research into engaging post structures,
    hooks, and content angles.
    """,
    llm=groq_llm,
    verbose=True
)