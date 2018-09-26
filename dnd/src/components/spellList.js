import React, { Component } from "react";
import { connect } from "react-redux";
import { fetchSpells, VisibilityFilters } from "../actions/spellActions";
import Spell from "./spell";

class SpellList extends Component {
	componentDidMount() {
		this.props.dispatch(fetchSpells());
	}

	getVisibleSpells = (spells, filter) => {
		let filtered_spells = Array.from(spells);

		switch (filter.level) {
			case VisibilityFilters.SHOW_ALL:
				break;
			case VisibilityFilters.SHOW_CANTRIP:
				filtered_spells = filtered_spells.filter(s => s.level === 0);
				break;
			case VisibilityFilters.SHOW_FIRST:
				filtered_spells = filtered_spells.filter(s => s.level === 1);
				break;
			case VisibilityFilters.SHOW_SECOND:
				filtered_spells = filtered_spells.filter(s => s.level === 2);
				break;
			case VisibilityFilters.SHOW_THIRD:
				filtered_spells = filtered_spells.filter(s => s.level === 3);
				break;
			case VisibilityFilters.SHOW_FOURTH:
				filtered_spells = filtered_spells.filter(s => s.level === 4);
				break;
			case VisibilityFilters.SHOW_FIFTH:
				filtered_spells = filtered_spells.filter(s => s.level === 5);
				break;
			case VisibilityFilters.SHOW_SIXTH:
				filtered_spells = filtered_spells.filter(s => s.level === 6);
				break;
			case VisibilityFilters.SHOW_SEVENTH:
				filtered_spells = filtered_spells.filter(s => s.level === 7);
				break;
			case VisibilityFilters.SHOW_EIGHTH:
				filtered_spells = filtered_spells.filter(s => s.level === 8);
				break;
			case VisibilityFilters.SHOW_NINTH:
				filtered_spells = filtered_spells.filter(s => s.level === 9);
				break;
			default:
				throw new Error("Invalid level filter: " + filter.level);
		}

		switch (filter.school) {
			case VisibilityFilters.SHOW_ALL:
				break;
			case VisibilityFilters.SHOW_ABJURATION:
				filtered_spells = filtered_spells.filter(s => s.school === "AB");
				break;
			case VisibilityFilters.SHOW_CONJURATION:
				filtered_spells = filtered_spells.filter(s => s.school === "CO");
				break;
			case VisibilityFilters.SHOW_DIVINATION:
				filtered_spells = filtered_spells.filter(s => s.school === "DI");
				break;
			case VisibilityFilters.SHOW_ENCHANTMENT:
				filtered_spells = filtered_spells.filter(s => s.school === "EN");
				break;
			case VisibilityFilters.SHOW_EVOCATION:
				filtered_spells = filtered_spells.filter(s => s.school === "EV");
				break;
			case VisibilityFilters.SHOW_ILLUSION:
				filtered_spells = filtered_spells.filter(s => s.school === "IL");
				break;
			case VisibilityFilters.SHOW_NECROMANCY:
				filtered_spells = filtered_spells.filter(s => s.school === "NE");
				break;
			case VisibilityFilters.SHOW_TRANSMUTATION:
				filtered_spells = filtered_spells.filter(s => s.school === "TR");
				break;
			default:
				throw new Error("Invalid school filter: " + filter.school);
		}

		switch (filter.concentration) {
			case VisibilityFilters.SHOW_ALL:
				break;
			case VisibilityFilters.SHOW_CONCENTRATION:
				filtered_spells = filtered_spells.filter(s => s.duration.toLowerCase().includes("concentration"));
				break;
			case VisibilityFilters.HIDE_CONCENTRATION:
				filtered_spells = filtered_spells.filter(s => !s.duration.toLowerCase().includes("concentration"));
				break;
			default:
				throw new Error("Invalid concentration filter: " + filter.concentration)
		}

		switch (filter.ritual) {
			case VisibilityFilters.SHOW_ALL:
				break;
			case VisibilityFilters.SHOW_RITUAL:
				filtered_spells = filtered_spells.filter(s => s.ritual);
				break;
			case VisibilityFilters.HIDE_RITUAL:
				filtered_spells = filtered_spells.filter(s => !s.ritual);
				break;
			default:
				throw new Error("Invalid ritual filter: " + filter.ritual)
		}

		switch (filter.components) {
			case VisibilityFilters.SHOW_ALL:
				break;
			case VisibilityFilters.HIDE_VERBAL:
				filtered_spells = filtered_spells.filter(s => !s.verbal);
				break;
			case VisibilityFilters.HIDE_SOMATIC:
				filtered_spells = filtered_spells.filter(s => !s.somatic);
				break;
			case VisibilityFilters.HIDE_MATERIAL:
				filtered_spells = filtered_spells.filter(s => !s.material);
				break;
			default:
				throw new Error("Invalid components filter: " + filter.components)
		}

		switch (filter.castingTime) {
			case VisibilityFilters.SHOW_ALL:
				break;
			case VisibilityFilters.SHOW_ACTION:
				filtered_spells = filtered_spells.filter(s => s.casting_time.toLowerCase().includes("1 action"));
				break;
			case VisibilityFilters.SHOW_BONUS_ACTION:
				filtered_spells = filtered_spells.filter(s => s.casting_time.toLowerCase() === "1 bonus action");
				break;
			case VisibilityFilters.SHOW_REACTION:
				filtered_spells = filtered_spells.filter(s => s.casting_time.toLowerCase().includes("1 reaction"));
				break;
			case VisibilityFilters.SHOW_OTHER_ACTION:
				filtered_spells = filtered_spells.filter(s =>
					s.casting_time.toLowerCase().includes("minute") ||
					s.casting_time.toLowerCase().includes("hour"));
				break;
			default:
				throw new Error("Invalid castingTime filter: " + filter.castingTime);
		}
		return filtered_spells;
	};

	render() {
		const { spells, filter } = this.props;

		if (spells.error) {
			return <div>ERROR! { spells.error.message }</div>
		}

		if (spells.loading) {
			return <div>Loading...</div>
		}

		if (!spells.items) return (<p>No Spells</p>)

		return (
			<div className="spellList">
				{ this.getVisibleSpells(spells.items, filter).map((spell, index) =>
					<Spell className="spellItem" key={index} data={spell} />
				)}
			</div>
		);
	}
}

const mapStateToProps = state => ({
	filter: state.spellReducer.visibilityFilter,
	spells: state.spellReducer.spells,
	loading: state.spellReducer.loading,
	error: state.spellReducer.error,
});

export default connect(mapStateToProps)(SpellList);
