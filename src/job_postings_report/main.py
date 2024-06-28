#!/usr/bin/env python
from crew import JobPostingsReportCrew
from dotenv import load_dotenv
import agentops

load_dotenv()

def run():
    role = input("Enter Specific Job Title: ")
    area = input("Enter location of Job search: ")
    
    inputs = {
        'role': role,
        'area': area
    }
    agentops.init()
    result = JobPostingsReportCrew().crew().kickoff(inputs=inputs)
    print("Analysis: ")
    print(result)
    agentops.end_session('Success')

if __name__ == "__main__":
    run()
