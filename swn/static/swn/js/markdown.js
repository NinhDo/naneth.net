var converter;

$("document").ready(() => {
	let md_field = $("#notes")[0];
	let raw_field = $("#markdown")[0];
	let rawText = md_field.value;
	converter = new showdown.Converter();
	let convertedText = converter.makeHtml(rawText);
	raw_field.innerHTML = convertedText;
	md_field.classList.add("hidden");
	raw_field.classList.remove("hidden");
});

$(function() {
	$("#notes_form").areYouSure();
})

function toggleMarkdown(button) {
	let raw_field = $("#notes")[0];
	let md_field = $("#markdown")[0];
	let icon = button;
	let rawText = raw_field.value;
	let convertedText = converter.makeHtml(rawText);
	md_field.innerHTML = convertedText;
	if (md_field.classList.contains("hidden")) { // If editing
		raw_field.classList.add("hidden");
		md_field.classList.remove("hidden");
		icon.innerHTML = "<i class=\"fas fa-edit\"></i>";
		saveNotes();
	} else { // If text
		md_field.classList.add("hidden");
		raw_field.classList.remove("hidden");
		icon.innerHTML = "<i class=\"fas fa-save\"></i>";
	}
}

function saveNotes() {
	let form = $("#notes_form");
	$.ajax({
		url: form.attr("data-save-url"),
		type: form.attr("method"),
		data: form.serialize(),
		dataType: "json",
		success: data => {
			if(data.error_message) {
				alert(data.error_message);
			}
		}
	});
	form.trigger('reinitialize.areYouSure');
}
