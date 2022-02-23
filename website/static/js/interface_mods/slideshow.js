let hero_section = document.querySelector('#hero_section')
let full_imgs = hero_section.querySelectorAll('.right_col img')

let buttons = hero_section.querySelectorAll('.slide_dot')
let slides = hero_section.querySelectorAll('.slide_ctnr')

for (let elem of buttons){
    elem.addEventListener('click', mod_slide, false)
}

var curr_slide = slides[0]
var curr_img = full_imgs[0]
var curr_index = 0
function mod_slide(event){
    if (event.target.dataset.slide_index==curr_index){
        return
    }

    curr_index = event.target.dataset.slide_index

    for (let elem of buttons){
        if (elem.dataset.slide_index==curr_index){
            elem.dataset.active = "true"
        } else {
            elem.dataset.active = "false"
        }
    }

    let old_slide = curr_slide
    let old_img = curr_img

    curr_slide = slides[curr_index]
    curr_img = full_imgs[curr_index]
    
    old_img.style.display = 'none'
    curr_img.style.display = 'block'


    old_slide.style.display = 'none'
    curr_slide.style.display = 'flex'
}

// const slideshow_clock = new THREE.Clock()
// let clocking = function(){
//     let curr_time = slideshow_clock.getElapsedTime()

//     if (curr_time < 9 && curr_time > 8 ){
//         slide_dots[slide_index].click()
//         slideshow_clock.start()
//         slide_index += 1;
//         if (slide_index >= slide_dots.length){
//             slide_index = 0
//         }
//     }
    
//     requestAnimationFrame(clocking)
// }
// clocking();


