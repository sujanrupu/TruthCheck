import React from "react";

const UrlInput = ({ url, setUrl, handleUrlSubmit }) => (
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
);

export default UrlInput;
