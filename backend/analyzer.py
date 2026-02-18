import os
import cohere
from dotenv import load_dotenv

load_dotenv()


co = cohere.Client(os.getenv("COHERE_API_KEY"))

def run_research_tool(transcript_text):
    """
    Latest Chat API ka upyog karke transcript analyze kar rahe hain.
    Variable names ko fix kiya gaya hai taaki 'not defined' error na aaye.
    """
    
    prompt_content = f"""
    Please perform a professional analysis on the following earnings transcript.
    Extract the following data into a structured report:
    
    1. Management Tone: (Optimistic, Cautious, Neutral, or Pessimistic)
    2. Confidence Level: (High, Medium, or Low)
    3. Key Positives: (3 to 5 points)
    4. Key Challenges: (3 to 5 points)
    5. Forward Guidance: (Revenue/Margin outlook)
    6. Growth Initiatives: (2 to 3 strategic points)

    Constraint: If any data is missing, state 'Information not available'.
    
    Transcript:
    {transcript_text[:6000]}
    """

    try:
        
        response = co.chat(
            model='command-a-vision-07-2025',
            message=prompt_content,
            temperature=0.2
        )
        
        return response.text
        
    except Exception as e:
        print(f"Detailed Trace: {str(e)}")
        return "The analysis engine is currently unavailable. Please check your API key status."