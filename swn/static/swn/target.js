window.onload = () => {
	addHoverListeners();
};

function addHoverListeners() {
	let hexes = document.getElementsByClassName("hex");
	for(let i = 0; i < hexes.length; i++) {
		hexes[i].addEventListener("mouseenter", (event) => {
			let rows = document.getElementsByClassName(hexes[i].classList[1]);
			if (rows) {
				for(let n = 1; n < rows.length; n++) {
					rows[n].classList.add("selected");
				}
			}
		});
		hexes[i].addEventListener("mouseleave", (event) => {
			let rows = document.getElementsByClassName(hexes[i].classList[1]);
			if(rows) {
				for(let n = 1; n < rows.length; n++) {
					rows[n].classList.remove("selected");
				}
			}
		});
	}
}

function filter(hex) {
	let tablerows = document.getElementsByClassName("systemTable")[0].children[1].children;
	let hexlength = document.getElementsByClassName(hex).length;
	if(hexlength > 1) {
		for(let i = 0; i < tablerows.length; i++) {
			if(tablerows[i].classList.contains(hex)) {
				tablerows[i].style.display = "table-row";
			} else {
				tablerows[i].style.display = "none";
			}
		}
	} else {
		for(let i = 0; i < tablerows.length; i++) {
			tablerows[i].style.display = "table-row";
		}
	}
}
