let backButton = document.querySelector('.apply-button')
let applyButton = document.querySelector('#apply-new-password')
let message = document.querySelector('.message')
alert('isdhjfoisuju;')
backButton.addEventListener('click', ()=>{
   location.href = urlIndex
})

applyButton.addEventListener('click', ()=>{
   let form = document.querySelector('.change-password-form')
   let formData = new FormData(form);
   fetch(urlForm, {
      method: 'POST',
      body: formData
   })
       .then(response => response.json())
       .then(data => {
          if (data.registered == 'true'){
             if (data.reg){
                message.textContent = data.message
             }else {
                message.textContent = data.message
             }
          }else {
             alert('Сначала нужно зарегистрироваться')
             location.href = urlIndex
          }

       })
       .catch(() => {
          message.textContent = 'Ошибка сервера, пожалуйста, попробуйте позже'
       });
})

