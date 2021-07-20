let appt_btns = document.querySelectorAll('.appointment_btn')
    for (let btn of appt_btns){
        btn.addEventListener('click', redir_appt, false)
    }
function redir_appt(){
    window.location.href = "/contact";
}