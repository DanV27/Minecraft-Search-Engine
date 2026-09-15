import "./App.css";

{/*npm --prefix /Users/daniel/Desktop/Minecraft-Search-Engine/minesearchReact run dev*/}


function App(props) {
  return (
    <>
      <header>
        <h1>MineSearch</h1>
          <form>
              <label htmlFor="userInput">Search: </label>
              <input type="text" id="userInput" name="search"/><br/>
              <button id="submitBtn" type="button">Search</button>
              <br/>

              <label htmlFor="displayText">Topics</label><br/>

              <ul id="displayText"></ul>

          </form>
      </header>
    </>
  );
}

export default App;