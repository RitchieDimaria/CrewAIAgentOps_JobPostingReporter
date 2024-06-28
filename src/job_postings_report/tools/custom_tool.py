from crewai_tools import BaseTool
import os
import requests
import json
class jobpostingstool(BaseTool):
    name: str = "Job Postings Fetcher"
    description: str = (
        "Fetches many of the relevant job postings from specific area and job title using adzuna API. Use only once and hand data to next agent"
    )

    def _run(self, role: str, area: str) -> str:
        
        API_URL = 'https://api.adzuna.com/v1/api/jobs/ca/search/1'
        app_id = os.environ.get('ARDZUNO_ID')
        app_key = os.environ.get('ARDZUNO_KEY')
        params = {
            'app_id': app_id,
            'app_key': app_key,
            'results_per_page': 15,
            'what': role,
            'where': area,
            'content-type': 'application/json'
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            response = requests.get(API_URL, params=params).text
            unparsed = json.loads(response)
            data = unparsed['results']
            for i in range(0, len(data)-1):
                try:
                    data[i].pop('adref')
                    data[i].pop('__CLASS__')
                    data[i].pop('id')
                    data[i].pop('longitude')
                    data[i].pop('latitude')
                    data[i].pop('category')
                except:
                    continue
            return data
        else:
            print(f"Failed to get job postings: {response.status_code}")
            raise Exception("Error fetching job postings")

