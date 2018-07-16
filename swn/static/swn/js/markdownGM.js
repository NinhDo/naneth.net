var converter;

$("document").ready(() => {
	let noteField = $("#gmNotes")[0];
	let textField = $("#gmMarkdown")[0];
	let rawText = noteField.value;
	converter = new showdown.Converter();
	let convertedText = converter.makeHtml(rawText);
	textField.innerHTML = convertedText;
	noteField.classList.add("hidden");
	textField.classList.remove("hidden");
});

$(function() {
	$("#gmNotes").areYouSure();
})

function toggleMarkdown() {
	let noteField = $("#gmNotes")[0];
	let textField = $("#gmMarkdown")[0];
	let button = $("#editButton")[0];
	let rawText = noteField.value;
	let convertedText = converter.makeHtml(rawText);
	textField.innerHTML = convertedText;
	if (noteField.classList.contains("hidden")) {
		textField.classList.add("hidden");
		noteField.classList.remove("hidden");
		editButton.innerHTML = "Save";
	} else {
		noteField.classList.add("hidden");
		textField.classList.remove("hidden");
		editButton.innerHTML = "Edit";
	}
}
