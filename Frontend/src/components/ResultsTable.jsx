import React from "react";

const ResultsTable = ({ response }) => (
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
          const correctedInfoText = correctInfo.replace(/http[^\s]+/g, "").trim();

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
);

export default ResultsTable;
