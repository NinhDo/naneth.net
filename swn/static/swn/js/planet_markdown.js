var converter;
$("document").ready(() => {
	let planet_notes = $("#planet_notes")[0];
	converter = new showdown.Converter();
	Array.from(planet_notes.children).forEach(child => {
		let md_field = child.children[2];
		let raw_field = child.children[3];
		let raw_text = raw_field.value;
		let converted_text = converter.makeHtml(raw_text);
		md_field.innerHTML = converted_text;
		raw_field.classList.add("hidden");
	});
})

$(function() {
	$("#planet_form").areYouSure();
})

function toggleMarkdown(button) {
	console.log("markdown toggled")
	let target = $(button).parent().parent().get(0);
	let icon = button;
	let md_field = target.children[2];
	let raw_field = target.children[3];
	let raw_text = raw_field.value;
	let converted_text = converter.makeHtml(raw_text);
	md_field.innerHTML = converted_text;
	if(md_field.classList.contains("hidden")) { // If editing
		console.log("disabling editing");
		raw_field.classList.add("hidden");
		md_field.classList.remove("hidden");
		icon.innerHTML = "<i class=\"fas fa-edit\"></i>"
		saveNotes();
	} else { // If normal view
		console.log("enabling editing");
		md_field.classList.add("hidden");
		raw_field.classList.remove("hidden");
		icon.innerHTML = "<i class=\"fas fa-save\"></i>"
	}
}

function saveNotes() {
	console.log("saving notes");
	let form = $("#planet_form");
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
