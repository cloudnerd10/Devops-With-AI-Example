import os
import sys
from langchain_google_genai import GoogleGenerativeAI

def analyze_logs(log_file):
    with open(log_file, 'r') as f:
        logs = f.read()
        # Analyze the logs here
        print("Log Analysis: ")
        print(logs)
        llm = GoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyA0jm_RIEoh-G2wncDR8e7v5r84pDSGdUU")
        print(
            llm.invoke(logs)
        )

if __name__ == "__main__":
    log_file = sys.argv[1]
    analyze_logs(log_file)
