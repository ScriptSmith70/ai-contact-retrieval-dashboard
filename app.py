# app.py
import streamlit as st
import pandas as pd
from data_processing import load_csv, save_to_google_sheets
from search_api import perform_web_search
from llm_extraction import extract_information_from_search

st.title("AI Contact Information Retrieval Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    data = load_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.write(data.head())

# Input for Query Template
st.sidebar.header("Enter Query Template")
query_template = st.sidebar.text_input(
    "Example: 'Get the email, phone number, and address for {entity}'"
)

# Process each entity with refined search and extraction
if uploaded_file and query_template:
    results = []
    for entity in data.iloc[:, 0]:  # Assuming the first column has entity names
        # Generate a specific query for each entity with refined keywords
        query = query_template.replace("{entity}", entity)
        
        # Perform the web search for this specific query
        search_results = perform_web_search(query)
        
        # Extract information based on the search results
        extracted_info = extract_information_from_search(search_results, entity, query)
        
        # Append the result for this entity
        results.append({"Entity": entity, "Extracted Info": extracted_info})
    
    # Display results in a table
    results_df = pd.DataFrame(results)
    st.write("Extracted Contact Information", results_df)

    # Option to save results to Google Sheets
    sheet_id = st.text_input("Enter Google Sheet ID to save results")
    sheet_range = st.text_input("Enter Sheet Range (e.g., 'Sheet1!A1')")
    if st.button("Save to Google Sheets"):
        if sheet_id and sheet_range:
            save_to_google_sheets(sheet_id, sheet_range, results_df)
            st.success("Results saved to Google Sheets!")
        else:
            st.error("Please provide a valid Google Sheet ID and range.")
