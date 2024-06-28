# JobPostingsReport Crew

Welcome to the JobPostingsReport Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. 

This project uses a requirements.txt file for dependencies

Navagate to root of directory

```bash
python -m venv venv
```

Activate virtual environment with

```bash
source venv/bin/activate
```

Install all dependencies (This may take a few minutes)

```bash
pip install -r requirements.txt
```
**Next you must create your own .env file in the root directory and add your own keys.**

- `OPENAI_API_KEY = <KEY GOES HERE>`
- `ARDZUNO_ID = <KEY GOES HERE>`
- `ARDZUNO_KEY = <KEY GOES HERE>`
- `AGENTOPS_API_KEY = <KEY GOES HERE>`
- `GROQ_API_KEY = <KEY GOES HERE>`

NOTE: All keys are free simply go make an account and use each id and key. The exception being OPENAI but you could just replace that llm with groq to run the code 

Feel free to modify these files

- Modify `src/job_postings_report/config/agents.yaml` to define your agents
- Modify `src/job_postings_report/config/tasks.yaml` to define your tasks
- Modify `src/job_postings_report/crew.py` to add your own logic, tools and specific args
- Modify `src/job_postings_report/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution run this line from the root of the directory

```bash
python src/job_postings_report/main.py
```

or navigate to the the src/job_postings_report directory

```bash
python main.py
```


This example, unmodified, will run the create a `report.md` file.

## Understanding Your Crew

The Job_Postings_Report Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

Thanks for reading!

A program by Richard Dimaria