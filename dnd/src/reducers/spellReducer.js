import {
	FETCH_SPELLS_BEGIN,
	FETCH_SPELLS_SUCCESS,
	FETCH_SPELLS_FAILURE,
	SET_VISIBILITY_FILTER,
	VisibilityFilters
} from "../actions/spellActions";

const initialState = {
	visibilityFilter: VisibilityFilters.SHOW_ALL,
	loading: false,
	error: null,
	spells: []
}

export default function spellReducer(state = initialState, action) {
	switch (action.type) {
		case SET_VISIBILITY_FILTER:
			return {
				...state,
				visibilityFilter: action.payload.filter
			};
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
				spells: action.payload.spells
			}
		case FETCH_SPELLS_FAILURE:
			return {
				...state,
				loading: false,
				error: action.payload.error,
				spells: []
			}
		default:
			return state;
	}
}
