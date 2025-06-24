# 🎥🧠 YT Videos to Blog Page using CrewAI Agents

This project uses **CrewAI** agents to automatically **analyze YouTube videos** and convert them into **engaging blog posts**. With intelligent agent collaboration and tool integration, the system mimics how a human researcher and writer would collaborate — but fully automated.

---

## 🚀 Features

- 🤖 Multi-agent system powered by [CrewAI]
- 📺 Extracts and understands YouTube video content
- ✍️ Converts AI/ML/Tech videos into readable blog posts
- 🔌 Plug-and-play Gemini API support (Google Generative AI)
- 🛠️ Uses tools like `yt_tool` for video transcription

---

## 🧠 Agents

### 🔍 Blog Researcher
- **Role**: Extracts insights and transcripts from relevant YouTube videos
- **Skills**: Specialized in AI, ML, GenAI, and Data Science topics

### ✍️ Blog Writer
- **Role**: Writes high-quality tech blogs from video insights
- **Skills**: Simplifies complex topics into engaging articles

---

## 📦 Requirements

- Python 3.9+
- pip

### 📦 Install Dependencies

```bash
pip install crewai crewai_tools google-generativeai

Environment Setup
import os

os.environ["GEMINI_API_KEY"] = "your-gemini-api-key"
os.environ["GEMINI_MODEL_NAME"] = "gemini-1.5-pro-latest"

How to Run

python crew.py

Use Cases
Generate blogs from tech conference videos

Summarize educational YouTube content

Auto-blogger for AI and data science channels


