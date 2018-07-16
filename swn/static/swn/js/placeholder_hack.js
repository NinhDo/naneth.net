window.onload = () => {
	addPlaceHolders();
};

function addPlaceHolders() {
	document.getElementById("id_username").placeholder = "ConnorWOO69";
	if(document.getElementById("id_password"))
		document.getElementById("id_password").placeholder = "SecretSecret";
}
