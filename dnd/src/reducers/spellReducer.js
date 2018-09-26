import { combineReducers } from "redux";
import {
	FETCH_SPELLS_BEGIN,
	FETCH_SPELLS_SUCCESS,
	FETCH_SPELLS_FAILURE,
	SET_VISIBILITY_FILTER,
	VisibilityFilters
} from "../actions/spellActions";

function visibilityFilter(
	state = {
		"level": VisibilityFilters.SHOW_ALL,
		"school": VisibilityFilters.SHOW_ALL,

		"concentration": VisibilityFilters.SHOW_ALL,
		"ritual": VisibilityFilters.SHOW_ALL,

		"components": VisibilityFilters.SHOW_ALL,

		"castingTime": VisibilityFilters.SHOW_ALL,

		"class": VisibilityFilters.SHOW_ALL,
	},
	action
) {
	switch (action.type) {
		case SET_VISIBILITY_FILTER:
			return {
				...state,
				[action.payload.type]: action.payload.filter
			}
		default:
			return state;
	}
}

function spells(
	state = {
		loading: false,
		error: null,
		items: []
	}, action
) {
	switch (action.type) {
		case FETCH_SPELLS_BEGIN:
			return {
				...state,
				loading: true,
				error: null
			}
		case FETCH_SPELLS_SUCCESS:
			return {
				...state,
				loading: false,
				items: action.payload.spells
			}
		case FETCH_SPELLS_FAILURE:
			return {
				...state,
				loading: false,
				error: action.payload.error,
				items: []
			}
		default:
			return state;
	}
}

export default combineReducers({
	spells,
	visibilityFilter
})
