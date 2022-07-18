const form = document.getElementById("password_form")
const checkbox = form.querySelector('#id_auto_password')
const helpTexts = form.querySelector('.helptext')
const password1 = form.querySelector('#id_new_password1')
const passwordLabel1 = form.querySelector("label[for='id_new_password1']")
const password2 = form.querySelector('#id_new_password2')
const passwordLabel2 = form.querySelector("label[for='id_new_password2']")

checkbox.addEventListener('click', (e)=>{
    if(e.target.checked){
        password1.removeAttribute('required')
        password1.style.display = 'none'
        passwordLabel1.style.display = 'none'
        password2.removeAttribute('required')
        password2.style.display = 'none'
        passwordLabel2.style.display = 'none'
        helpTexts.style.display = 'none'
    }
    else{
        password1.setAttribute('required','true')
        password1.style.display = 'block'
        passwordLabel1.style.display = 'block'
        password2.setAttribute('required','true')
        password2.style.display = 'block'
        passwordLabel2.style.display = 'block'
        helpTexts.style.display = 'block'
        
    }
})