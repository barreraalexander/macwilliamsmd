let submit_btn = document.querySelector('#contact_submit')
if (submit_btn){
    let form_elem = document.querySelector('#client_form')
    submit_btn.addEventListener('click', function(){
        // alert('ran')
        form_elem.submit()
    })
}