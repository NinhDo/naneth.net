var edit = false;

function toggleMarkdown() {
  let noteField = document.getElementById("playerNotes");
  let textField = document.getElementById("playerMarkdown");
  let button = document.getElementById("editButton");
  let rawText = noteField.value;
  let converter = new showdown.Converter();
  let convertedText = converter.makeHtml(rawText);
  textField.innerHTML = convertedText;
  if (edit) {
    textField.style.display = "none";
    noteField.style.display = "block";
    editButton.innerHTML = "Save";
  } else {
    noteField.style.display = "none";
    textField.style.display = "block";
    editButton.innerHTML = "Edit";
  }
  edit = !edit;
}
