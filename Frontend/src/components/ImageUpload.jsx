import React from "react";

const ImageUpload = ({ setImageFile, handleImageSubmit }) => (
  <div>
    <h2 className="text-xl font-medium text-white mb-2">Upload Image</h2>
    <input
      type="file"
      className="w-full p-3 bg-[#2C4A63] text-white border border-gray-300 rounded-lg mb-4"
      accept="image/*"
      onChange={(e) => setImageFile(e.target.files[0])}
    />
    <button
      onClick={handleImageSubmit}
      className="w-full bg-purple-500 text-white p-2 rounded-lg hover:bg-purple-600"
    >
      Check Image
    </button>
  </div>
);

export default ImageUpload;
