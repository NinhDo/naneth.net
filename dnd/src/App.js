import React, { Component } from 'react';
import './App.css';
import SpellList from "./components/spellList";

class App extends Component {
	render() {
		return (
			<div className="App">
				<SpellList />
			</div>
		);
	}
}

export default App;
