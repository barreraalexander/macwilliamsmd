// const insurances_ctnr_tl = gsap.timeline()
const insurances_ctnr = document.querySelector('.insurances_ctnr')
const insurances = insurances_ctnr.querySelectorAll('.insurance')

const insurances_ctnr_options = {
    root: null,
    threshold: .1,
}

const insurances_observer = new IntersectionObserver(function(entries, insurances_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            insurances_tl.resume()
        } else {

        }
    })
}, insurances_ctnr_options);

insurances_observer.observe(insurances_ctnr)


const insurances_tl = gsap.timeline()
insurances_tl.pause()

for (let insurance of insurances){
    insurances_tl.to(insurance,
        {
            duration: .25,
            clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
            transform: 'translate(0px, -10px)'
        }      
    ), "-=1"
}
