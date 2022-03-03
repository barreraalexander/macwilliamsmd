let hero_section = document.querySelector('#hero_section')
let full_imgs = hero_section.querySelectorAll('.right_col img')

let buttons = hero_section.querySelectorAll('.slide_dot')
let slides = hero_section.querySelectorAll('.slide_ctnr')

for (let elem of buttons){
    elem.addEventListener('click', mod_slide, false)
}


let slide_tl = gsap.timeline(
    {
        paused: true,
    }
)

var curr_slide = slides[0]
var curr_img = full_imgs[0]
var curr_index = 0
function mod_slide(event){

    if (event.isTrusted){
        if (slideshow_clock){
            slideshow_clock.stop()
        }
    }


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

    slide_tl.to(
        [old_slide, old_img], {
            duration: .5,
            opacity: 0,
            display: 'none',
        }
    ), 0

    slide_tl.to(
        [curr_slide, curr_img], {
            duration: .5,
            opacity: 1,
            display: 'flex',
        }
    )
    slide_tl.resume()
}

var slide_index = 0
const slideshow_clock = new THREE.Clock()
let clocking = function(){

    let curr_time = slideshow_clock.getElapsedTime()

    if (curr_time < 6 && curr_time > 5 ){
        slideshow_clock.start()
        buttons[slide_index].click()


        slide_index +=  1;
        if (slide_index >= buttons.length){
            slide_index = 0
        }

    }
    
    requestAnimationFrame(clocking)
}
clocking();


