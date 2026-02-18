import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [analysis, setAnalysis] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  
const handleUpload = async () => {
    if (!file) {
      alert("Please select a valid PDF document for analysis.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setAnalysis("");

    try {
      
      const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://127.0.0.1:8000";
      
      const response = await axios.post(`${backendUrl}/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      if (response.data.analysis) {
        setAnalysis(response.data.analysis);
      } else if (response.data.error) {
        setAnalysis("Processing Error: " + response.data.error);
      }
    } catch (error) {
      console.error("Connection failed:", error);
      setAnalysis("Unable to connect to the research server.");
    } finally {
      setLoading(false);
    }
};

  return (
    <div className="portal-container">
      <header className="portal-header">
        <h1>Research Portal Slice</h1>
        <p className="portal-description">Financial Analysis Tool: Earnings Commentary Summary</p>
      </header>

      <main className="portal-content">
        <div className="upload-container">
          <label className="input-label">Select Earnings Transcript (PDF)</label>
          <input type="file" accept=".pdf" onChange={handleFileChange} className="file-input" />
          <button onClick={handleUpload} disabled={loading} className="analyze-button">
            {loading ? "Analyzing Data..." : "Generate Research Summary"}
          </button>
        </div>

        {analysis && (
          <div className="output-container">
            <h3 className="output-title">Extracted Research Intelligence</h3>
            <div className="output-content">
              <pre>{analysis}</pre>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;