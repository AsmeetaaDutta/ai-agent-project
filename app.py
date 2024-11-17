import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from io import StringIO


def connect_to_google_sheet(credentials_path):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)
    return client

def process_data_with_langchain(df, column_name, prompt_template, api_key):

    llm = OpenAI(api_key=api_key)
    chain = LLMChain(llm=llm, prompt=prompt_template)

    results = []

    for entity in df[column_name]:
        result = chain.run(company=entity, web_results="Sample web results text for now")
        results.append(result)
    
    df["Extracted Data"] = results
    return df

st.title("Information Extraction Dashboard")
st.write("Upload a CSV or connect to a Google Sheet, and retrieve specific information for each entity.")

option = st.selectbox("Choose data source:", ("Upload CSV", "Google Sheet"))

if option == "Upload CSV":
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:", df.head())

elif option == "Google Sheet":
    credentials_path = st.text_input("Enter path to Google API credentials JSON")
    sheet_url = st.text_input("Enter Google Sheet URL")

    if credentials_path and sheet_url:
        client = connect_to_google_sheet(credentials_path)
        spreadsheet = client.open_by_url(sheet_url)
        sheet = spreadsheet.get_worksheet(0)
        data = sheet.get_all_records()
        df = pd.DataFrame(data)
        st.write("Data Preview:", df.head())

if "df" in locals():
    column_name = st.selectbox("Select the column with entities (e.g., companies):", df.columns)

    prompt_input = st.text_input("Enter custom prompt (use {company} as placeholder):", 
                                 "Get me the email address of {company}")
    
    if st.button("Process Data"):
        if prompt_input and column_name:
            api_key = st.text_input("Enter your OpenAI API key", type="password")

            prompt_template = PromptTemplate(
                input_variables=["company", "web_results"],
                template=prompt_input + " from the following web results: {web_results}"
            )
            
            with st.spinner("Processing..."):
                df = process_data_with_langchain(df, column_name, prompt_template, api_key)
                st.success("Data processed successfully!")
                st.write("Extracted Information", df)

            csv = df.to_csv(index=False)
            st.download_button("Download CSV", csv, "extracted_results.csv", "text/csv")
