var about_section = document.querySelector('#about_section')
var ul_ctnr = document.querySelector('.ul_ctnr')
var descr1 = document.querySelector('.description1_ctnr')
var about_row = document.querySelector('.about_row')
var doc_ctnr = document.querySelector('.about_doctor_ctnr')

const descr_options = {
    root: null,
    threshold : .25,
}

const description_observer = new IntersectionObserver(function(entries, description_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            entry.target.style.transition = "3s";
            entry.target.style.opacity = "1";

        } else {
            entry.target.style.opacity = "0";
        }
    })
}, descr_options);

description_observer.observe(descr1)
description_observer.observe(about_row)

const ul_options = {
    root : null,
    threshold : 1
}


const ul_observer = new IntersectionObserver(function(entries, ul_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            console.log('here now')
            entry.target.style.transition = '1.5s';
            entry.target.style.filter = "grayscale(0)";
        } else {
            console.log('leaving')
            entry.target.style.filter = "grayscale(100%)";
        }
    })
}, ul_options);

ul_observer.observe(ul_ctnr)
ul_observer.observe(doc_ctnr)