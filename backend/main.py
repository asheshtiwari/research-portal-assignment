from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from processor import DocumentEngine
from analyzer import run_research_tool 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.get("/")
def health_check():
    return {"status": "active", "message": "Server is operational"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Document must be in PDF format")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    try:
        # Save file to local storage
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Extract text from the PDF
        engine = DocumentEngine(file_path)
        raw_text = engine.extract_text()
        
        if not raw_text or len(raw_text.strip()) == 0:
            return {"error": "The document appears to be empty or unreadable"}

        # This calls the LLM with our structured logic
        analysis_result = run_research_tool(raw_text)
        
        return {
            "filename": file.filename,
            "status": "success",
            "analysis": analysis_result
        }

    except Exception as e:
        # Return a generic error message to the client
        return {"error": f"An error occurred during processing: {str(e)}"}
    finally:
        file.file.close()