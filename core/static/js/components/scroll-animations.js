//ELEMENTOS
const aboutTitle = document.querySelector('.main-text._first')
const aboutText = document.querySelector('.main-text._about-text')

const knowledgeTitle = document.querySelector('.second-title._knowledge-title')
const knowledgeItems = document.querySelectorAll('.knowledge-items')

const skillsTitle = document.querySelector('.second-title._skills')
const skillsItems = document.querySelectorAll('.skills-items')

const sectionProjects = document.querySelector('.main-section._projects')
const loading = document.querySelector('.loading-element')

sectionProjects.style.display = 'none';

//Get quantitys
const qk = Number(document.querySelector('#quantity-knowledge').textContent)
const qs = Number(document.querySelector('#quantity-skill').textContent)

//FUNCTIONS

window.addEventListener('scroll', () => {
    console.log(scrollY)

        if (scrollY > 400){
            aboutTitle.classList.add('animation-on')
        }
        if (scrollY > 450){
            aboutText.classList.add('animation-on')
        }
        if (scrollY > 900){
            knowledgeTitle.classList.add('animation-on')
        }
        if (scrollY > 1400){
            for (var i = 0; i < qk; i++){
                knowledgeItems[i].classList.add('animation-opacity')
            }
        }
        if (scrollY > 1700){
            skillsTitle.classList.add('animation-on')
        }
        if (scrollY > 1800){
            for (var i = 0; i < qs; i++) {
                skillsItems[i].classList.add('animation-opacity')
            }
        }
        if (scrollY > 2000) {
            setTimeout(() => {
                loading.style.display = 'none';
                sectionProjects.style.display = 'flex';
            }, 3000)
        }

})
