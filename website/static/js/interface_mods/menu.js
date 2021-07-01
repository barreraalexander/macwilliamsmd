let nav_button = document.querySelector('#hamburger')
if (nav_button){
    nav_button.addEventListener('click', mod_menu, false)
}

function mod_menu(){
    let hidden_menu = document.querySelector('#hidden_menu')

    hidden_menu.style.display = "block"

}