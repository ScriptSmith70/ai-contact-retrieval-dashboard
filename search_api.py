# search_api.py
import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def perform_web_search(query):
    """Perform a web search using SerpAPI and handle any potential errors."""
    api_key = os.getenv("SERPAPI_KEY")
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
    }
    try:
        response = requests.get("https://serpapi.com/search", params=params)
        response.raise_for_status()
        return response.json().get("organic_results", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Search API error: {e}")
        return []
