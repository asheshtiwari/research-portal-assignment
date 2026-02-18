import fitz  
import os

class DocumentEngine:
    """
    Handles extraction of text from uploaded research documents.
    Focuses on maintaining structural integrity of transcripts.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        
        if not os.path.exists(self.file_path):
            return "Error: File not found."

        text = ""
        try:
            with fitz.open(self.file_path) as doc:
                for page in doc:
                    text += page.get_text()
            return text
        except Exception as e:
            # Log the specific error for debugging
            print(f"Extraction failed: {e}")
            return ""