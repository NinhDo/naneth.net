import React, { Component } from "react";
import { connect } from "react-redux";
import { VisibilityFilters, setVisibilityFilter } from "../actions/spellActions";

class SpellFilter extends Component {



	render() {
		return (
			<div className="spellFilter">
				<label htmlFor="levelFilter">Spell Level </label>
				<select name="levelFilter" className="levelFilter"
					onChange={
						(e) =>
							this.props.dispatch(
								setVisibilityFilter("level", e.target.value)
							)
					}>
					<option value={ VisibilityFilters.SHOW_ALL }>All</option>
					<option value={ VisibilityFilters.SHOW_CANTRIP }>Cantrip</option>
					<option value={ VisibilityFilters.SHOW_FIRST }>1st</option>
					<option value={ VisibilityFilters.SHOW_SECOND }>2nd</option>
					<option value={ VisibilityFilters.SHOW_THIRD }>3rd</option>
					<option value={ VisibilityFilters.SHOW_FOURTH }>4th</option>
					<option value={ VisibilityFilters.SHOW_FIFTH }>5th</option>
					<option value={ VisibilityFilters.SHOW_SIXTH }>6th</option>
					<option value={ VisibilityFilters.SHOW_SEVENTH }>7th</option>
					<option value={ VisibilityFilters.SHOW_EIGHTH }>8th</option>
					<option value={ VisibilityFilters.SHOW_NINTH }>9th</option>
				</select>

				<label htmlFor="schoolFilter">School </label>
				<select name="schoolFilter" className="schoolFilter"
					onChange={
						(e) =>
							this.props.dispatch(
								setVisibilityFilter("school", e.target.value)
							)
					}>
					<option value={ VisibilityFilters.SHOW_ALL }>All</option>
					<option value={ VisibilityFilters.SHOW_ABJURATION }>Abjuration</option>
					<option value={ VisibilityFilters.SHOW_CONJURATION }>Conjuration</option>
					<option value={ VisibilityFilters.SHOW_DIVINATION }>Divination</option>
					<option value={ VisibilityFilters.SHOW_ENCHANTMENT }>Enchantment</option>
					<option value={ VisibilityFilters.SHOW_EVOCATION }>Evocation</option>
					<option value={ VisibilityFilters.SHOW_ILLUSION }>Illusion</option>
					<option value={ VisibilityFilters.SHOW_NECROMANCY }>Necromancy</option>
					<option value={ VisibilityFilters.SHOW_TRANSMUTATION }>Transmutation</option>
				</select>

				<label htmlFor="concentrationFilter">Concentration </label>
				<select name="concentrationFilter" className="concentrationFilter"
					onChange={
						(e) =>
							this.props.dispatch(
								setVisibilityFilter("concentration", e.target.value)
							)
					}>
					<option value={ VisibilityFilters.SHOW_ALL }>All</option>
					<option value={ VisibilityFilters.SHOW_CONCENTRATION }>Yes</option>
					<option value={ VisibilityFilters.HIDE_CONCENTRATION }>No</option>
				</select>

				<label htmlFor="ritualFilter">Ritual </label>
				<select name="ritualFilter" className="ritualFilter"
					onChange={
						(e) =>
							this.props.dispatch(
								setVisibilityFilter("ritual", e.target.value)
							)
					}>
					<option value={ VisibilityFilters.SHOW_ALL }>All</option>
					<option value={ VisibilityFilters.SHOW_RITUAL }>Yes</option>
					<option value={ VisibilityFilters.HIDE_RITUAL }>No</option>
				</select>

				<label htmlFor="componentsFilter">Components </label>
				<select name="componentsFilter" className="componentsFilter"
					onChange={
						(e) =>
							this.props.dispatch(
								setVisibilityFilter("components", e.target.value)
							)
					}>
					<option value={ VisibilityFilters.SHOW_ALL }>All</option>
					<option value={ VisibilityFilters.HIDE_VERBAL }>No verbal</option>
					<option value={ VisibilityFilters.HIDE_SOMATIC }>No somatic</option>
					<option value={ VisibilityFilters.HIDE_MATERIAL }>No material</option>
				</select>

				<label htmlFor="castingTimeFilter">Casting Time </label>
				<select name="castingTimeFilter" className="castingTimeFilter"
					onChange={
						(e) =>
							this.props.dispatch(
								setVisibilityFilter("castingTime", e.target.value)
							)
					}>
					<option value={ VisibilityFilters.SHOW_ALL }>All</option>
					<option value={ VisibilityFilters.SHOW_ACTION }>1 Action</option>
					<option value={ VisibilityFilters.SHOW_BONUS_ACTION }>1 Bonus Action</option>
					<option value={ VisibilityFilters.SHOW_REACTION }>1 Reaction</option>
					<option value={ VisibilityFilters.SHOW_OTHER_ACTION }>Other</option>
				</select>
			</div>
		);
	}
}

const mapStateToProps = state => ({
	filter: state.spellReducer.filter
});

export default connect(mapStateToProps)(SpellFilter);
