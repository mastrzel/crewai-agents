from crewai import Agent, Task
import os
from dotenv import load_dotenv
from crewai import Crew, Process

load_dotenv(override=True)

azure_model=os.getenv("AZURE_MODEL_NAME")

# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  verbose=True,
  llm=azure_model,
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)

# Task for the researcher
research_task = Task(
  description='Identify the next big trend in AI',
  agent=researcher,  # Assigning the task to the researcher
  expected_output='next big trends in AI'
)


# Instantiate your crew
tech_crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  process=Process.sequential,  # Tasks will be executed one after the other
  verbose=True,
)

# Begin the task execution
tech_crew.kickoff()