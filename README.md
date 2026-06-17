# 🤖 LinkedIn AI Agents with CrewAI

An AI multi-agent system that automatically researches trending topics 
and generates LinkedIn content strategies using CrewAI and Groq's 
LLaMA 3.3-70b model.

## 🧠 Agents
- **Researcher** — Finds latest trends and insights on any topic
- **Strategist** — Transforms research into LinkedIn post outlines with hook, key points & CTA

## 🛠️ Tech Stack
- [CrewAI](https://crewai.com) — Multi-agent orchestration
- [Groq](https://groq.com) — Ultra-fast LLM inference
- LLaMA 3.3-70b — Underlying language model
- Python 3.12

## 🚀 Setup
1. Clone the repo
2. Create a virtual environment and install dependencies:
   pip install -r requirements.txt
3. Add your Groq API key to .env:
   GROQ_API_KEY=your_key_here
4. Run:
   python main.py

## 📁 Project Structure
crew_ai/
├── agents/
│   ├── researcher.py
│   └── strategist.py
├── tasks/
│   ├── research_task.py
│   └── strategy_task.py
├── main.py
└── .env
