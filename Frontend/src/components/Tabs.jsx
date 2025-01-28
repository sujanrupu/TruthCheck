import React from "react";

const Tabs = ({ activeTab, setActiveTab }) => {
  return (
    <div className="flex space-x-4 mb-6">
      {["text", "url", "pdf"].map((tab) => (
        <button
          key={tab}
          className={`px-4 py-2 text-lg font-medium ${
            activeTab === tab ? "border-b-2 border-purple-500 text-purple-500" : "text-white"
          }`}
          onClick={() => setActiveTab(tab)}
        >
          {tab.toUpperCase()}
        </button>
      ))}
    </div>
  );
};

export default Tabs;
