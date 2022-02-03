let doctors_section = document.querySelector('#doctors_section');
let doctor_text_ctnrs = document.querySelectorAll('.doctor_panel_ctnr');


const doc_options = {
    root: null,
    threshold : .25,
}

const doctor_observer = new IntersectionObserver(function(entries, doctor_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            entry.target.style.transition = "3s";
            entry.target.style.opacity = "1";

        } else {
            entry.target.style.opacity = "0";
        }
    })
}, doc_options);

for (let elem of doctor_text_ctnrs){
    doctor_observer.observe(elem)
}