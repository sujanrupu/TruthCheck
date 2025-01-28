import React from "react";

const PdfUpload = ({ setPdfFile, handlePdfSubmit }) => (
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
);

export default PdfUpload;
