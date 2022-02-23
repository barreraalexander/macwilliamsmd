const nav_button = document.querySelector('#hamburger')

const hidden_menu = document.querySelector('#hidden_menu')
const empty = document.querySelector('.empty')
const empty_p = document.querySelector('.empty p')
const nav_elem = document.querySelector('#hidden_menu nav')


if (nav_button){
    nav_button.addEventListener('click', mod_menu, false)
    empty.addEventListener('click', mod_menu, false)
    empty_p.addEventListener('click', mod_menu, false)
}

function mod_menu(event){
    if (event.target==nav_button){
        menu_tween.play()
    } else if (event.target==empty || event.target==empty_p){
        menu_tween.reverse()
    }
}


const menu_tween = gsap.timeline(
    {
        paused: true,
    }
)


menu_tween.to(
    hidden_menu,
    {
        duration: .3,
        display: 'flex',
        opacity: 1,
    }
,), 0


menu_tween.to(
    empty,
    {
        duration: .5,
        left: "0em",
        ease:Sine.easeInOut
    },
    1
),
    
menu_tween.to(
    nav_elem,
    {
        duration: .5,
        right: "0em",
        ease:Sine.easeInOut
    },
    1
)