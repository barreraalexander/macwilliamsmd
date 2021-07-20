let lastKnownScrollPosition = 0;
let ticking = false;



// function check_no_scroll(scrollPos){
//   setTimeout(function(){
//     divider.classList.add("enlarge_div")
//     var scroll_alert = document.createElement("p")
//     var alert_text = document.createTextNode("Please Scroll Down")
//     scroll_alert.appendChild(alert_text)
//     scroll_alert.classList.add("scroll_alert")
//     divider.appendChild(scroll_alert)
//   }, 6000)
// }

// if (divider){
//   check_no_scroll()
// }

function mod_doctor_cards(scrollPos){
    let cards = document.querySelectorAll('.doctor_panel_lg_ctnr')
    if (scrollPos >= 80 && scrollPos <= 200){
        for (let card of cards){
            card.classList.add('apply_lift')
        }
    }
}


document.addEventListener('scroll', function(e) {
  lastKnownScrollPosition = window.scrollY;
  if (!ticking) {
    window.requestAnimationFrame(function() {
        if (screen.width >= 1200){
            mod_doctor_cards(lastKnownScrollPosition)
        }


    ticking = false;
    });
    ticking = true;
  }
});