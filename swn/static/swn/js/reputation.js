var reputation_dict = {
	"neutral": "lightgray",
	"friendly": "lightgreen",
	"unfriendly": "lightred",
	"ally": "green",
	"hostile": "red",
}

window.onload = () => {
	let cells = document.getElementsByClassName("reputation");
	for (let i = 0; i < cells.length; i++) {
		for (let reputation in reputation_dict) {
			if (cells[i].textContent.toLowerCase() == reputation) {
				cells[i].style.backgroundColor = reputation_dict[reputation];
			}
		}
	}
}
