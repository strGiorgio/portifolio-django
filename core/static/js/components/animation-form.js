var background = window.document.querySelector('.main-section._contacts');
var form = window.document.querySelector('.main-form');

form.addEventListener('mouseover', formEntered);
form.addEventListener('mouseout', formOut);

function formEntered(){
    background.style.backgroundImage = "url('https://i.imgur.com/61ElS4l.png')"
    
};
function formOut(){
    background.style.backgroundImage = "url('https://i.imgur.com/nLNGlvi.png')"
};
