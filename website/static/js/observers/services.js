var services_section = document.querySelector('#services_section');
var text_groups = services_section.querySelectorAll('.text_group')
var service_grid = document.querySelector('.services_grid_ctnr')
var top_button = document.querySelector('#back_to_top')

const serv_options = {
    root: null,
    threshold : .10,
}

const serv_observer = new IntersectionObserver(function(entries, serv_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            entry.target.style.transition = "3.5s";
            entry.target.style.opacity = "1";

        } else {
            // entry.target.style.opacity = "0";
        }
    })
}, serv_options);

for (let elem of text_groups){
    serv_observer.observe(elem)
}

serv_observer.observe(service_grid)



const scroll_btn = {
    root: null,
    threshold: .10,
}

const scroll_btn_observer = new IntersectionObserver(function(entries, serv_observer){
    entries.forEach(entry => {
        if (! entry.isIntersecting){
            top_button.style.transition = "2s";
            top_button.style.opacity = "1"

            setTimeout(function(){
                top_button.style.display = "flex"
            }, 3000)


        } else {
            top_button.style.opacity = "0"

            setTimeout(function(){
                top_button.style.display = "none"
            }, 2000)

        }
    })
})


scroll_btn_observer.observe(service_grid)


// show back to the top button

