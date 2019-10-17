import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <form action="http://127.0.0.1:8000/api/v1/songs" method="GET">
          <div className="field">
            <label className="label has-text-left has-text-light is-uppercase">Artist Name</label>
            <div className="field has-addons">
              <div className="control">
                <input placeholder="e.g. Bob Dylan" id="artist" name="artist" type="text" className="input is-large" />
              </div>
              <div className="control">
                <input type="submit" value="Write Song" className="button is-large is-primary" />
              </div>
            </div>
          </div>
        </form>
      </header>
    </div>
  );
}

export default App;
