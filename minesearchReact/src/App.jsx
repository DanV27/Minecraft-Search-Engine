import { useState } from "react";
import "./App.css";

{/*npm --prefix /Users/daniel/Desktop/Minecraft-Search-Engine/minesearchReact run dev*/}

function App() {
  // 1. React States to manage your input, search status, and results array
  const [inputValue, setInputValue] = useState("");
  const [results, setResults] = useState([]);
  const [statusMessage, setStatusMessage] = useState("");

  // 2. The React function to handle the search submission
  const handleSearch = async (e) => {
    e.preventDefault(); // Prevents the form from refreshing the page

    if (inputValue.trim() !== "") {
      setStatusMessage("Searching...");
      setResults([]); // Clear previous results

      try {
        // Sends the data to your POST route on the Flask backend
        const response = await fetch("http://127.0.0.1:5000/", { // Use your exact Flask port (usually 5000)
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({ userInput: inputValue }),
            });

        // Parse the list array coming back from basic_search()
        const resultsArray = await response.json();
        setStatusMessage(""); // Clear the status message

        if (resultsArray.length === 0) {
          setStatusMessage("No results found.");
        } else {
          setResults(resultsArray); // Save the results array into state
        }
      } catch (error) {
        console.error("Connection error:", error);
        setStatusMessage("Error: Could not process search.");
      }
    } else {
      setStatusMessage("Please type something first!");
    }
  };

  return (
    <div className="page">
      <header>
        <h1>MineSearch</h1>
        <p className="subtitle">Search the Minecraft wiki</p>

        {/* 3. Connect the form submit event to our function */}
        <form className="search-form" onSubmit={handleSearch}>
          <div className="search-bar">
            <input
              type="text"
              id="userInput"
              name="search"
              placeholder="Search for a topic..."
              value={inputValue} // Binds the input value to React state
              onChange={(e) => setInputValue(e.target.value)} // Updates state when typing
            />
            {/* Note: changed type to "submit" so pressing Enter inside the input also works! */}
            <button type="submit">Search</button>
          </div>

          {/* 4. Display status message if one exists */}
          {statusMessage && (
            <p className={`status ${statusMessage.includes("Error") ? "status-error" : ""}`}>
              {statusMessage}
            </p>
          )}

          {results.length > 0 && (
            <div className="results-wrap">
              <h2>Topics</h2>
              <ul className="results">
                {/* 5. Loop through the results array and generate <li> elements dynamically */}
                {results.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>
          )}
        </form>
      </header>
    </div>
  );
}

export default App;
