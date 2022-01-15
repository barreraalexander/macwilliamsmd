let index_section = document.querySelector('#hero_section')

if (index_section){
    var slide_dots = index_section.querySelectorAll('.slide_dot')
    for (let dot of slide_dots){
        dot.addEventListener('click', mod_slide, false)
    }
}

let curr_slide_id = "welcome_slide_ctnr";
function mod_slide(){
    if (this.dataset.panel_id != curr_slide_id){
        
        let unselected_dot = index_section.querySelector(`.slide_dot[data-panel_id='${curr_slide_id}']`)
        this.dataset.active = "true";
        unselected_dot.dataset.active = "false";   
        
        let unselected_slide = index_section.querySelector(`#${unselected_dot.dataset.panel_id}`)
        unselected_slide.classList.add('apply_disappear')
        unselected_slide.classList.remove('remove_disappear')
        
        let selected_slide = index_section.querySelector(`#${this.dataset.panel_id}`)
        selected_slide.classList.add('remove_disappear')
        selected_slide.classList.remove('apply_disappear')
    
        let unselected_full_img = index_section.querySelector(`#${unselected_dot.dataset.full_img_id}`)
        unselected_full_img.classList.add('apply_disappear')
        unselected_full_img.classList.remove('remove_disappear')
        
        let selected_full_img = index_section.querySelector(`#${this.dataset.full_img_id}`)
        selected_full_img.classList.add('remove_disappear')
        selected_full_img.classList.remove('apply_disappear')

        let unselected_slide_text = index_section.querySelector(`#${unselected_dot.dataset.text_id}`)
        unselected_slide_text.classList.add('apply_disappear')
        unselected_slide_text.classList.remove('remove_disappear')
        
        let selected_slide_text = index_section.querySelector(`#${this.dataset.text_id}`)
        selected_slide_text.classList.add('remove_disappear')
        selected_slide_text.classList.remove('apply_disappear')
    
        curr_slide_id = this.dataset.panel_id
        slideshow_clock.stop()
          
    }
}


var slide_index = 1;
const slideshow_clock = new THREE.Clock()
let clocking = function(){
    let curr_time = slideshow_clock.getElapsedTime()

    if (curr_time < 9 && curr_time > 8 ){
        slide_dots[slide_index].click()
        slideshow_clock.start()
        slide_index += 1;
        if (slide_index >= slide_dots.length){
            slide_index = 0
        }
    }
    
    requestAnimationFrame(clocking)
}
clocking();


