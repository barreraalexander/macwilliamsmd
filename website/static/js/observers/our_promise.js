const our_promise_section = document.querySelector('#our_promise_section')
const gif_ctnr = our_promise_section.querySelector('.gif_ctnr')
const mission_statement_ctnr = our_promise_section.querySelector('.mission_statement_ctnr')

const mission_statement_ctnr_options = {
    root: null,
    threshold: .4, 
}

const mission_observer = new IntersectionObserver(function(entries, mission_observer){
    entries.forEach(entry => {
        if (entry.isIntersecting){
            our_promise_tl.resume()
            // alert('here')
        } else {

        }
    })
}, mission_statement_ctnr_options);


mission_observer.observe(our_promise_section)

const our_promise_tl = gsap.timeline()

our_promise_tl.pause()


our_promise_tl.to(
    gif_ctnr,
    {
        duration: .8,
        filter: "grayscale(100)",

    }
), "-=1"



our_promise_tl.to(
    mission_statement_ctnr,
    {
        delay: 2.5,
        duration: 1,
        clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',

    }
), "-=1"



// const tl = gsap.timeline()
