from crewai import Agent
from crewAI.tools import yt_tool
import os
os.environ["GEMINI_API_KEY"] = "" 
os.environ["GEMINI_MODEL_NAME"] = "gemini-1.5-flash" 
# create a senior blog content researcher agent

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    # memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science,Machine Learning and GEN AI and providing suggestion "
    ),
    tools=[yt_tool],
    allow_delegation=True
)

#createing a senior blog content writer agent

blog_writer=Agent(
    role="Blog Writer",
    goal="write a blog on the topic {topic} based on the transcription provided by the researcher",
    verbose=True,   
    # memory=True,
    backstory=(
        "Expert in writing blogs on AI Data Science,Machine Learning and GEN AI based on the transcription provided by the researcher"
    ),
    tools=[yt_tool],
    allow_delegation=False
)