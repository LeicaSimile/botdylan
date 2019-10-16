import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <form action="http://127.0.0.1:8000/api/v1/songs" method="GET">
          <input id="artist" name="artist" type="text" />
          <input type="submit" value="Write Song" />
        </form>
      </header>
    </div>
  );
}

export default App;
