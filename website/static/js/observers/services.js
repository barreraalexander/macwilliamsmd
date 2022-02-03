var services_section = document.querySelector('#services_section');
var text_groups = services_section.querySelectorAll('.text_group')

const serv_options = {
    root: null,
    threshold : .33,
}

const serv_observer = new IntersectionObserver(function(entries, serv_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            entry.target.style.transition = "2s";
            entry.target.style.opacity = "1";

        } else {
            // entry.target.style.opacity = "0";
        }
    })
}, serv_options);

for (let elem of text_groups){
    serv_observer.observe(elem)
}