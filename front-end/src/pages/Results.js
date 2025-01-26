import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";

const Results = () => {
  const [results, setResults] = useState([]);  // State to store the results
  const [loading, setLoading] = useState(false);  // State for loading indicator
  const [error, setError] = useState(null);  // State for error handling
  const location = useLocation();  // Get the current URL location

  const queryParams = new URLSearchParams(location.search);
  const searchQuery = queryParams.get("q");  // Get the query parameter "q"

  useEffect(() => {
    if (searchQuery) {
      setLoading(true);
      setError(null);

      // Fetch data based on the search query
      fetch(`http://25.63.219.231:8000/query`, {
        method: "POST",
        
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        },

        // Adding body or contents to send
        body: JSON.stringify({
            "query": searchQuery,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          setResults(data);  // Set the results
          setLoading(false);  // Stop loading
          console.log(data)
        })
        .catch((err) => {
          setError("Error fetching results.");
          setLoading(false);  // Stop loading in case of error
        });
    }
  }, [searchQuery]);  // Re-run when the search query changes

  return (
    <div className="bg-[#121212] min-h-screen">
      <header className="App-header bg-[#121212]">
        <h1 className="text-Roboto text-white">Search Results</h1>

        {loading && <div>Loading...</div>}
        {error && <div className="text-red-500">{error}</div>}
        {!loading && !error && results.length === 0 && <div>No results found.</div>}

        {/* Display search results */}
        {!loading && !error && results.length > 0 && (
          <ul>
            {results.map((result, index) => (
              <li key={index} className="text-white">
                <h3>{result.title}</h3>
                <p>{result.description}</p>
              </li>
            ))}
          </ul>
        )}
      </header>
    </div>
  );
};

export default Results;
