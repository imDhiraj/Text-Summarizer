import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API token and URL from environment variables
API_TOKEN = os.getenv("Hugging_Face_Token")
API_URL = os.getenv("Hugging_Face_URL")

def summarize_text(text: str) -> str:
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": text})
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Extract the summary from the response
        summary = response.json()[0]["summary_text"]
        return summary
    
    except requests.exceptions.RequestException as e:
        print(f"Error calling Hugging Face API: {e}")
        return "Error generating summary. Please try again."