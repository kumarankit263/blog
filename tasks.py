from crewai import Task
from crewAI.agents import blog_researcher, blog_writer
from crewAI.tools import yt_tool
#Research Task
research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel video."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  tools=[yt_tool],
  agent=blog_researcher,
)


# Writing Task
writing_task=Task(
    description=(
        "Write a blog on the topic {topic} based on the transcription provided by the researcher",
        "The blog should be engaging and informative, suitable for publication on a tech blog.",
    ),
    expected_output='A well-structured blog post with an introduction, body, and conclusion.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)