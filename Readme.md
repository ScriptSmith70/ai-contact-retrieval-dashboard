AI Contact Information Retrieval Dashboard
This project is a dashboard that allows users to find contact information for companies. It uses web search and AI to find emails, phone numbers, and other contact details.

Project Description
This app allows users to:

Upload a CSV file with a list of companies.
Specify search queries to retrieve contact information (e.g., "Get the email for {company}").
Display or save results to a Google Sheet.
Setup Instructions
To run this app on your computer, follow these steps:

Clone the Repository:
git clone https://github.com/ScriptSmith70/ai-contact-retrieval-dashboard.git
cd ai-contact-retrieval-dashboard
Create a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install Dependencies:
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file with your API keys:
makefile
Copy code
SERPAPI_KEY=your_serpapi_key
COHERE_API_KEY=your_cohere_api_key
GOOGLE_SHEETS_CREDENTIALS=path/to/your/google_credentials.json
Get API keys for SerpAPI and Cohere.
Download a Google service account JSON file with access to Google Sheets API.
Run the App:
streamlit run app.py
Usage Guide
Upload a CSV File or Connect Google Sheets.
Enter a Query like "Get the email for {entity}".
View Results and save them to Google Sheets if needed.
Optional Features
Advanced Queries: Extract multiple fields at once, e.g., "Get the email and phone for {entity}".
Google Sheets Output: Save results directly to Google Sheets.
Error Handling: Displays errors when APIs fail or data isn’t found.
Demo Video
Watch the video walkthrough here: https://www.loom.com/share/3ad853449f9e4c6fb7a154ef7a8a6bef?sid=56cba1d5-04b4-4eb4-8642-3d2b5b410f75
