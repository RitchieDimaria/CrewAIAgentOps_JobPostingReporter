from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import jobpostingstool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import agentops
from agentops import track_agent
import os

agentops.init()

@CrewBase
class JobPostingsReportCrew():
	"""JobPostingsReport crew for analyzing and reporting details on upcoming jobpostings"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	def __init__(self):
		self.groq_llm = ChatGroq(
			temperature=0,
			groq_api_key=os.environ.get('GROQ_API_KEY'),
			model_name='llama3-8b-8192'
		)
		self.openai_llm = ChatOpenAI(
			temperature=0,
			api_key=os.environ.get('OPENAI_API_KEY'),
			model="gpt-4",
			max_retries=2
		)
	
	@track_agent(name="Job_Posting_Fetcher")
	@agent
	def Job_Posting_Fetcher(self) -> Agent:
		return Agent(
			config=self.agents_config['job_scout'],
			tools=[jobpostingstool()], 
			allow_delegation=False,
			verbose=True,
			llm=self.groq_llm,
		)
	
	@track_agent(name="Job_Extractor")
	@agent
	def Job_Extractor(self) -> Agent:
		return Agent(
			config=self.agents_config['job_extractor'],
			allow_delegation=False,
			verbose=True,
			llm=self.groq_llm,
		)
	
	@track_agent(name="reporting_analyst")
	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			allow_delegation=False,
			llm=self.openai_llm,
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.Job_Posting_Fetcher(),
		)
	
	@task
	def extract_task(self) -> Task:
		return Task(
			config=self.tasks_config['extract_task'],
			agent=self.Job_Extractor(),
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.reporting_analyst(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the JobPostingsReport crew"""
		return Crew(
			agents=[self.Job_Posting_Fetcher(),self.Job_Extractor(),self.reporting_analyst()], 
			tasks=[self.research_task(),self.extract_task(),self.reporting_task()], 
			memory=False,
			process=Process.sequential,
			verbose=1,
		)