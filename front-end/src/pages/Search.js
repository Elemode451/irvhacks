import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import SearchBar from "../Components/SearchBar";

const Search = () => {
  const [searchQuery, setSearchQuery] = useState(""); // State to track the search query
  const navigate = useNavigate();

  // Function to handle search input (this is passed down to SearchBar)
  const handleSearch = (query) => {
    setSearchQuery(query); // Update the state with the new search query
    console.log("Search Query:", query); // Log the current search query

    // After the search is performed, navigate to the Results page with the search query
    navigate(`/results?q=${query}`);
  };

  return (
    <div className="bg-[#121212] min-h-screen">
      <header className="App-header bg-[#121212]">
        <h1 className="text-Roboto absolute top-[150px] text-white">
          How can I help you today?
        </h1>
        <div className="w-1/3 absolute top-[250px]">
          <SearchBar onSearch={handleSearch} />
        </div>
      </header>
    </div>
  );
};

export default Search;
