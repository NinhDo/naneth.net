/*
 * Action types
 */

export const FETCH_SPELLS_BEGIN = "FETCH_SPELLS_BEGIN";
export const FETCH_SPELLS_SUCCESS = "FETCH_SPELLS_SUCCESS";
export const FETCH_SPELLS_FAILURE = "FETCH_SPELLS_FAILURE";
export const SET_VISIBILITY_FILTER = "SET_VISIBILITY_FILTER";
/*
 * Other constraints
 */

export const VisibilityFilters = {
	SHOW_ALL: "SHOW_ALL",

	SHOW_ABJURATION: "SHOW_ABJURATION",
	SHOW_CONJURATION: "SHOW_CONJURATION",
	SHOW_DIVINATION: "SHOW_DIVINATION",
	SHOW_ENCHANTMENT: "SHOW_ENCHANTMENT",
	SHOW_EVOCATION: "SHOW_EVOCATION",
	SHOW_ILLUSION: "SHOW_ILLUSION",
	SHOW_NECROMANCY: "SHOW_NECROMANCY",
	SHOW_TRANSMUTATION: "SHOW_TRANSMUTATION",

	SHOW_BARD: "SHOW_BARD",
	SHOW_CLERIC: "SHOW_CLERIC",
	SHOW_DRUID: "SHOW_DRUID",
	SHOW_PALADIN: "SHOW_PALADIN",
	SHOW_RANGER: "SHOW_RANGER",
	SHOW_SORCERER: "SHOW_SORCERER",
	SHOW_WARLOCK: "SHOW_WARLOCK",
	SHOW_WIZARD: "SHOW_WIZARD"
};

/*
 * Action creators
 */

export function fetchSpells() {
	return dispatch => {
		dispatch(fetchSpellsBegin());
		return fetch("/dnd/spells/")
			.then(handleErrors)
			.then(response => response.json())
			.then(json => {
				dispatch(fetchSpellsSuccess(json));
				return json;
			})
			.catch(error => dispatch(fetchSpellsFailure(error)));
	};
}

function handleErrors(response) {
	if (!response.ok) {
		throw Error(response.statusText);
	}
	return response;
}

export const fetchSpellsBegin = () => ({
	type: FETCH_SPELLS_BEGIN
});

export const fetchSpellsSuccess = spells => ({
	type: FETCH_SPELLS_SUCCESS,
	payload: { spells }
});

export const fetchSpellsFailure = error => ({
	type: FETCH_SPELLS_FAILURE,
	payload: { error }
});

export const setVisibilityFilter = filter => ({
	type: SET_VISIBILITY_FILTER,
	payload: { filter }
});