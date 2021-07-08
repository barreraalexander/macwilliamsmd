let contact_submit = document.querySelector('#contact_submit')
if (contact_submit){
    let form_elem = document.querySelector('#contact_form')
    contact_submit.addEventListener('click', function(){
        form_elem.submit()
    })
}

let client_submit = document.querySelector('#new_client_submit')
if (client_submit){
    let form_elem = document.querySelector('#client_form')
    client_submit.addEventListener('click', function(){
        form_elem.submit()
    })
}