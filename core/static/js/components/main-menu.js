let show = true;
const toggleMenu = document.querySelector('.main-header')
const menu = document.querySelector('.main-menu')

function menuAction() {
    document.body.style.overflow = show ? "hidden" : "initial";
    menu.classList.toggle('on')
    toggleMenu.classList.toggle('toggle-menu')
    show = !show;
}

function closeMenu() {
    menu.classList.remove('on')
    toggleMenu.classList.remove('toggle-menu')
    document.body.style.overflow = "initial";
    show = !show;
}