# llm_extraction.py
import os
import re
import cohere
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

def extract_information_from_search(search_results, entity, query):
    """
    Use Cohere API to extract specific contact information from search results.
    Handles multiple types (emails, phone numbers, URLs) based on query input.
    """
    # Concatenate all search snippets into a single text block
    search_text = " ".join([result.get("snippet", "") for result in search_results])

    # Regex patterns for emails, phone numbers, and URLs
    patterns = {
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "phone": r"\+?\(?\d{1,4}\)?[\d\s-]{5,}",  # Matches various phone number formats
        "url": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    }

    # Initialize a variable to store extracted information
    extracted_info = ""

    # Apply regex pattern matching based on query
    if "email" in query.lower():
        emails = re.findall(patterns["email"], search_text)
        if emails:
            unique_emails = list(set(emails))
            extracted_info += "Emails: " + ", ".join(unique_emails) + "\n"

    if "phone" in query.lower():
        phones = re.findall(patterns["phone"], search_text)
        if phones:
            unique_phones = list(set(phones))
            extracted_info += "Phones: " + ", ".join(unique_phones) + "\n"

    if "url" in query.lower() or "support" in query.lower() or "contact" in query.lower():
        urls = re.findall(patterns["url"], search_text)
        if urls:
            unique_urls = list(set(urls))
            extracted_info += "Relevant Links: " + ", ".join(unique_urls) + "\n"

    # If pattern-based info was found, return it
    if extracted_info.strip():
        return extracted_info.strip()

    # Use Cohere to attempt extraction if no direct pattern match was found
    try:
        prompt = f"{query} for {entity}. Here are some details I found:\n\n{search_text}"
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=100,
            temperature=0.5
        )
        cohere_output = response.generations[0].text.strip()
        return cohere_output if cohere_output else "No specific information found"
    except Exception as e:
        st.error(f"Cohere API error: {e}")
        return "Error in extracting information"
