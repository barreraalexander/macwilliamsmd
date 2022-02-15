let current_href = window.location.href
let page = current_href.split('/')[-1]

let hidden_menu_lis = document.querySelectorAll('#hidden_menu li')


for (let elem of hidden_menu_lis){
    if (page){
        console.log(page)
    } else {
        console.log(hidden_menu_lis[0])
    }
}

// function mod_hidden_menu_li(){
//     // elem.dataset.active = ""
//     // event.target.dataset.active = "true"

// }

// alert('here')
// console.log(page)

if (current_href){

}