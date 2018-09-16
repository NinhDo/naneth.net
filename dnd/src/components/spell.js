import React, { Component } from "react";
import "../css/spell.scss";


export default class Spell extends Component {
	render() {
		const schools = {
			"AB": "Abjuration",
			"CO": "Conjuration",
			"DI": "Divination",
			"EN": "Enchantment",
			"EV": "Evocation",
			"IL": "Illusion",
			"NE": "Necromancy",
			"TR": "Transmutation",
		}
		let schoolLevel = ""
		// If cantrip, schoolLevel is SCHOOL Cantrip
		// Else it's Nth-level SCHOOL
		if (this.props.data.level === 0) {
			schoolLevel = `${schools[this.props.data.school]} Cantrip`
		} else {
			schoolLevel = `${this.props.data.level}${ordinal(this.props.data.level)}-level ${schools[this.props.data.school]}`
		}

		let components = ""
		if (this.props.data.verbal) components += "V, "
		if (this.props.data.somatic) components += "S, "
		if (this.props.data.material) components += `M (${this.props.data.material_material})`
		else {
			components = components.replace(/([,\s]+$)/g, ''); // remove trailing comma
		}
		let description = {
			__html: this.props.data.description
		}

		let higherLevelDescription;
		if (this.props.data.higher_level_description) {
			higherLevelDescription = <p className="higherLevelDescription"><b>At Higher Levels. </b>{ this.props.data.higher_level_description }</p>
		}

		return (
			<div className="spell">
				<div className="spellInfo">
					<span className="spellName">{ this.props.data.name }</span>
					<span className="spellSchoolLevel"><i>{ schoolLevel }</i></span>
					<span className="spellCastingTime"><b>Casting Time: </b>{ this.props.data.casting_time }</span>
					<span className="spellRange"><b>Range: </b>{ this.props.data.range }</span>
					<span className="spellComponents"><b>Components: </b>{ components }</span>
					<span className="spellDuration"><b>Duration: </b>{ this.props.data.duration }</span>
				</div>
				<div className="spellDescription">
					<p dangerouslySetInnerHTML={ description }/>
					{ higherLevelDescription }
				</div>
				<div className="spellBook"><i>{ this.props.data.book }</i></div>
			</div>
		);
	}
}

// Don't need top worry about multiple digits or 0, so this is fine for 1-9
function ordinal(n) {
	let o = ["th", "st", "nd", "rd"]
	return o[n > 3 ? 0 : n]
}
