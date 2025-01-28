import React, { useState } from 'react';
import axios from 'axios';

const SentenceChecker = () => {
  const [sentences, setSentences] = useState('');
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Reset error state
    const inputSentences = sentences.split('.').map((s) => s.trim()).filter((s) => s);

    try {
      const response = await axios.post('http://localhost:5000/check_url', {
        sentences: inputSentences,
      });
      setResults(response.data);
    } catch (error) {
      console.error('Error checking content:', error.response ? error.response.data : error.message);
      setError('An error occurred while processing the request.');
    }
  };

  return (
    <div className="p-4">
      <form onSubmit={handleSubmit} className="mb-4">
        <textarea
          className="w-full p-2 border rounded"
          rows="4"
          placeholder="Enter sentences here..."
          value={sentences}
          onChange={(e) => setSentences(e.target.value)}
        />
        <button
          type="submit"
          className="mt-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Submit
        </button>
      </form>

      {error && <div className="text-red-500">{error}</div>}

      {results.length > 0 && (
        <table className="w-full border-collapse border border-gray-300">
          <thead>
            <tr className="bg-gray-200">
              <th className="border border-gray-300 px-4 py-2">Incorrect Sentence</th>
              <th className="border border-gray-300 px-4 py-2">Correct Information</th>
              <th className="border border-gray-300 px-4 py-2">Source Website</th>
            </tr>
          </thead>
          <tbody>
            {results.map((result, index) => (
              !result.is_valid && (
                <tr key={index}>
                  <td className="border border-gray-300 px-4 py-2">{result.sentence}</td>
                  <td className="border border-gray-300 px-4 py-2">{result.correction || 'N/A'}</td>
                  <td className="border border-gray-300 px-4 py-2">
                    {result.source ? (
                      <a
                        href={result.source}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-blue-500 underline"
                      >
                        {result.source}
                      </a>
                    ) : 'N/A'}
                  </td>
                </tr>
              )
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default SentenceChecker;
