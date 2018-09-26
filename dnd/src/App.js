import React, { Component } from 'react';
import './App.css';
import SpellList from "./components/spellList";
import SpellFilter from "./components/spellFilter";

class App extends Component {
	render() {
		return (
			<div className="App">
				<SpellFilter />
				<SpellList />
			</div>
		);
	}
}

export default App;
