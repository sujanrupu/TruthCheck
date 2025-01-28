import React from "react";

const TextInput = ({ text, setText, handleTextSubmit }) => (
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
);

export default TextInput;
