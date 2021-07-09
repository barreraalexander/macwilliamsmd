let nav_button = document.querySelector('#hamburger')
if (nav_button){
    nav_button.addEventListener('click', mod_menu, false)
}


function mod_menu(){
    var hidden_menu = document.querySelector('#hidden_menu')
    var menu_status = hidden_menu.dataset.status

    if (menu_status=='closed'){
        hidden_menu.classList.remove('apply_hide_menu')
        hidden_menu.classList.add('apply_show_menu')
        hidden_menu.dataset.menu_status = 'open'
        window.addEventListener('click', check_target, false)

    //SECTION: REFERENCE TO slideshow_clock
        slideshow_clock.stop()

    } else if (menu_status=='open'){
        window.removeEventListener('click', check_target)
        menu_status = 'closed' 
    }
}


function check_target(event){
    if (event.target != hidden_menu &&
        event.target != nav_button &&
        event.target.parentNode != hidden_menu){
        hidden_menu.dataset.status = 'closed'
        hidden_menu.classList.remove('apply_show_menu')
        hidden_menu.classList.add('apply_hide_menu')
        menu_status = 'closed'
        window.removeEventListener('click', check_target)

    //SECTION: REFERENCE TO slideshow_clock
        slideshow_clock.start()

    }
}