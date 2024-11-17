import openai
import requests
import pandas as pd
from langchain import LLMChain, PromptTemplate
import time

openai.api_key = 'your_openai_api_key'

def perform_search(query):
    api_url = f"https://api.serpapi.com/search?q={query}&api_key=your_serpapi_key"
    response = requests.get(api_url)
    return response.json().get('organic_results', [])

def extract_info(search_results, prompt):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt + "\n\n" + "\n".join(search_results),
        max_tokens=100,
    )
    return response.choices[0].text.strip()

def run_agent(entities, query_template, fields_to_extract):
    extracted_data = []
    for entity in entities:
        query = query_template.format(company=entity)
        
        search_results = perform_search(query)
        prompt = f"Extract {', '.join(fields_to_extract)} for {entity} from the following results."
        extracted_info = extract_info(search_results, prompt)
        extracted_data.append([entity] + extracted_info.split(', '))
        time.sleep(1)

    return pd.DataFrame(extracted_data, columns=["Entity"] + fields_to_extract)
