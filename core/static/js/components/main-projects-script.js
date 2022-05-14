var n = 0

function lClick() {
    if (n > 0) {
        n -= 1
    } 
    else {
        n = 2
    }

    console.log(`${n}`)
    changeBg()
}
function rClick() {
    if (n < 2) {
        n += 1
    } 
    else {
        n = 0
    }
    console.log(`${n}`)
    changeBg()
}

function changeBg() {
    const background = document.querySelector('.main-section._projects')

    const projects1 = document.querySelector('.project-one'); 
    const projects2 = document.querySelector('.project-two');
    const projects3 = document.querySelector('.project-three');


    if (n == 0) {
        //Python Projects
        background.style.background= '#0C141D'
        projects1.style.display = "flex"
        projects2.style.display = "none"
        projects3.style.display = "none"
    } 
    else if (n == 1) {
        //Others Projects
        background.style.background= '#2A53DB'
        projects1.style.display = "none"
        projects2.style.display = "flex"
        projects3.style.display = "none"
    } 
    else {
        //GitHub
        background.style.background= '#322D28'
        projects1.style.display = "none"
        projects2.style.display = "none"
        projects3.style.display = "flex"
    }
}