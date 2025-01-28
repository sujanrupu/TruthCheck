import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './loader.css';

function App() {
  const [url, setUrl] = useState("");
  const [text, setText] = useState("");
  const [pdfFile, setPdfFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [activeTab, setActiveTab] = useState("text");
  const [loading, setLoading] = useState(false);  // Add loading state

  useEffect(() => {
    document.title = "TruthCheck";  // Set the title dynamically
  }, []);

  const [checked, setChecked] = useState(false); // Track if a check has been performed

  const handleTextSubmit = async () => {
    if (!text) {
      setErrorMessage("Please enter text in the Text tab.");
      return;
    }
    setErrorMessage(""); // Clear previous error
    setLoading(true); // Start loading
    setChecked(true); // Indicate that a check is being performed
    try {
      const result = await axios.post('https://news-backend-5j0p.onrender.com/check_text', { text });
      setResponse(result.data);
    } catch (error) {
      console.error('Error checking content:', error);
    } finally {
      setLoading(false); // Stop loading
    }
  };

  // Similarly update handleUrlSubmit and handlePdfSubmit
  const handleUrlSubmit = async () => {
    if (!url) {
      setErrorMessage("Please enter a URL in the URL tab.");
      return;
    }
    setErrorMessage("");
    setLoading(true);
    setChecked(true);
    try {
      const result = await axios.post('https://news-backend-5j0p.onrender.com/check_url', { url });
      setResponse(result.data);
    } catch (error) {
      console.error('Error checking content:', error);
    } finally {
      setLoading(false);
    }
  };

  const handlePdfSubmit = async () => {
    if (!pdfFile) {
      setErrorMessage("Please upload a PDF file in the PDF tab.");
      return;
    }
    setErrorMessage("");
    setLoading(true);
    setChecked(true);
    const formData = new FormData();
    formData.append('pdf', pdfFile);

    try {
      const result = await axios.post('https://news-backend-5j0p.onrender.com/check_pdf', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setResponse(result.data);
    } catch (error) {
      console.error('Error checking PDF:', error);
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="App min-h-screen bg-black flex items-center justify-center p-6 flex-col">
      <div className="w-full max-w-4xl bg-dark-sea-blue rounded-lg shadow-lg p-6 mb-6">
        <h1 className="text-3xl font-semibold text-white text-center mb-6">TruthCheck</h1>

        {/* Tabs Navigation */}
        <div className="flex space-x-4 mb-6">
          <button
            className={`px-4 py-2 text-lg font-medium ${activeTab === "text" ? "border-b-2 border-purple-500 text-purple-500" : "text-white"}`}
            onClick={() => setActiveTab("text")}
          >
            Text
          </button>
          <button
            className={`px-4 py-2 text-lg font-medium ${activeTab === "url" ? "border-b-2 border-purple-500 text-purple-500" : "text-white"}`}
            onClick={() => setActiveTab("url")}
          >
            URL
          </button>
          <button
            className={`px-4 py-2 text-lg font-medium ${activeTab === "pdf" ? "border-b-2 border-purple-500 text-purple-500" : "text-white"}`}
            onClick={() => setActiveTab("pdf")}
          >
            PDF
          </button>
        </div>

        {/* Error message */}
        {errorMessage && <p className="text-red-500 text-center mb-4">{errorMessage}</p>}

        {/* Tab Content */}
        {activeTab === "text" && (
          <div>
            <h2 className="text-xl font-medium text-white mb-2">Text Input</h2>
            <textarea
              className="w-full p-3 bg-[#2C4A63] text-white border border-gray-300 rounded-lg mb-4 focus:outline-none focus:border-purple-500"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Enter text to check"
              rows="6"
            />
            <button
              onClick={handleTextSubmit}
              className="w-full bg-purple-500 text-white p-2 rounded-lg hover:bg-purple-600"
            >
              Check Text
            </button>
          </div>
        )}

        {activeTab === "url" && (
          <div>
            <h2 className="text-xl font-medium text-white mb-2">URL Input</h2>
            <input
              className="w-full p-3 bg-[#2C4A63] text-white border border-gray-300 rounded-lg mb-4 focus:outline-none focus:border-purple-500"
              type="text"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="Enter URL to check"
            />
            <button
              onClick={handleUrlSubmit}
              className="w-full bg-purple-500 text-white p-2 rounded-lg hover:bg-purple-600"
            >
              Check URL
            </button>
          </div>
        )}

        {activeTab === "pdf" && (
          <div>
            <h2 className="text-xl font-medium text-white mb-2">Upload PDF</h2>
            <input
              type="file"
              className="w-full p-3 bg-[#2C4A63] text-white border border-gray-300 rounded-lg mb-4"
              accept=".pdf"
              onChange={(e) => setPdfFile(e.target.files[0])}
            />
            <button
              onClick={handlePdfSubmit}
              className="w-full bg-purple-500 text-white p-2 rounded-lg hover:bg-purple-600"
            >
              Check PDF
            </button>
          </div>
        )}

        {/* Loading Spinner */}
        {loading && (
          <div className="flex justify-center items-center mt-6">
            <div className="loader"></div>
          </div>
        )}

        {/* Table to display response */}
        {/* Table to display response */}
        {checked && !loading && response && response.length > 0 ? (
          <div className="mt-6">
            <h2 className="text-xl font-medium text-white mb-4">Results</h2>
            <table className="w-full table-auto border-collapse">
              <thead>
                <tr className="bg-purple-500 text-white">
                  <th className="px-4 py-2 border-b w-1/3">Incorrect Information</th>
                  <th className="px-4 py-2 border-b w-1/3">Correct Information</th>
                  <th className="px-4 py-2 border-b w-1/3">Source</th>
                </tr>
              </thead>
              <tbody>
                {response.map((item, idx) => {
                  const correctInfo = item[2].replace(/^No\.\s*/, "");
                  const sourceLink = correctInfo.match(/http[^\s]+/g);
                  const correctedInfoText = correctInfo.replace(/http[^\s]+/g, '').trim();

                  return (
                    <tr key={idx} className="border-b">
                      <td className="px-4 py-2 text-white">{item[1]}</td>
                      <td className="px-4 py-2 text-white">{correctedInfoText}</td>
                      <td className="px-4 py-2 text-white">
                        {sourceLink ? (
                          <a href={sourceLink[0]} target="_blank" rel="noopener noreferrer" className="text-blue-500">
                            {sourceLink[0]}
                          </a>
                        ) : (
                          "No source available"
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        ) : (
          checked && !loading && <p className="text-green-500 text-center mt-6">No incorrect information found</p>
        )}

      </div>

      {/* Footer */}
      <footer className="w-full bg-[#1C3A4A] text-center py-4 mt-6 fixed bottom-0">
        <p className="text-white">Developed by Sujan Ghosh</p>
      </footer>

    </div>

  );
}

export default App;
