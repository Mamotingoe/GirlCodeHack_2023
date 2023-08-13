const menuItems = document.querySelectorAll('.menu a');

menuItems.forEach(item => {
  item.addEventListener('click', function(event) {
    menuItems.forEach(item => item.classList.remove('active'));
    this.classList.add('active');
  });
});
