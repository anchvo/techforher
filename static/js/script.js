// Get elements
const menuToggle = document.getElementById('menu-toggle');
const menu = document.getElementById('menu');

// Toggle the menu visibility when the burger icon is clicked
menuToggle.addEventListener('click', function() {
    menu.classList.toggle('show'); // Toggle 'show' class to show/hide the menu
});

