function showMenu() {
  let header = document.getElementsByClassName('header')[0];
  if(header.classList.contains('responsive')) {
    header.classList.remove('responsive');
  } else {
    header.classList.add('responsive');
  }
}
