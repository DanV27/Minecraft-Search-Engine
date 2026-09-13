// 1. Select the HTML elements using their IDs
const button = document.getElementById('submitBtn');
const inputField = document.getElementById('userInput');
const outputList = document.getElementById('displayText'); // Now targets our <ul> element

// 2. Add an event listener to the button
button.addEventListener('click', async function() {
    // 3. Get the current value from the input box
    const inputValue = inputField.value;

    // 4. Send the value to Python and build the list elements
    if (inputValue.trim() !== "") {
        outputList.innerHTML = "<li>Searching...</li>"; // Clear old results and show status

        try {
            // Sends the data to your POST route on the same server
            const response = await fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ userInput: inputValue })
            });

            // Parse the list array coming back from basic_search()
            const resultsArray = await response.json();

            // Clear the "Searching..." text to prepare for actual data
            outputList.innerHTML = "";

            // Check if Python returned an empty list
            if (resultsArray.length === 0) {
                outputList.innerHTML = "<li>No results found.</li>";
            } else {
                // Loop through each item in the list and append it to the HTML
                resultsArray.forEach(item => {
                    const listItem = document.createElement('li');
                    listItem.textContent = item; // Sets the text to the search result string
                    outputList.appendChild(listItem);
                });
            }

        } catch (error) {
            console.error("Connection error:", error);
            outputList.innerHTML = "<li style='color: red;'>Error: Could not process search.</li>";
        }

    } else {
        outputList.innerHTML = "<li style='color: orange;'>Please type something first!</li>";
    }
});
