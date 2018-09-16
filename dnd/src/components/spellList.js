import React, { Component } from "react";
import { connect } from "react-redux";
import { fetchSpells } from "../actions/spellActions";
import Spell from "./spell";

class SpellList extends Component {
	componentDidMount() {
		this.props.dispatch(fetchSpells());
	}

	render() {
		const { error, loading, spells } = this.props;

		if (error) {
			return <div>ERROR! { error.message }</div>
		}

		if (loading) {
			return <div>Loading...</div>
		}

		if (spells.length === 0) return (<p>No Spells</p>)

		return (
			<div className="spellList">
				{ spells.map((spell, index) =>
					<Spell className="spellItem" key={index} data={spell} />
				)}
			</div>
		);
	}
}

const mapStateToProps = state => ({
	spells: state.spellReducer.spells,
	loading: state.spellReducer.loading,
	error: state.spellReducer.error,
});

export default connect(mapStateToProps)(SpellList);
