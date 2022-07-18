const checkbox = document.getElementById('id_auto_password')
const helpTexts = document.querySelectorAll('.helptext')
const password1 = document.getElementById('id_password1')
const passwordLabel1 = document.querySelector("label[for='id_password1']")
const password2 = document.getElementById('id_password2')
const passwordLabel2 = document.querySelector("label[for='id_password2']")

checkbox.addEventListener('click', (e)=>{
    if(e.target.checked){
        password1.removeAttribute('required')
        password1.style.display = 'none'
        passwordLabel1.style.display = 'none'
        password2.removeAttribute('required')
        password2.style.display = 'none'
        passwordLabel2.style.display = 'none'
        let reps = 1
        for (const el of helpTexts) {
            if (reps !== 1) el.style.display= 'none'
            reps++
        }
    }
    else{
        password1.setAttribute('required','true')
        password1.style.display = 'block'
        passwordLabel1.style.display = 'block'
        password2.setAttribute('required','true')
        password2.style.display = 'block'
        passwordLabel2.style.display = 'block'
        let reps = 1
        for (const el of helpTexts) {
            if (reps !== 1) el.style.display= 'block'
            reps++
        }
        
    }
})