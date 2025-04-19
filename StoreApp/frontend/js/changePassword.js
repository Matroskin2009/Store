let backButton = document.querySelector('.apply-button')
let applyButton = document.querySelector('#apply-new-password')
let message = document.querySelector('.message')
alert('isdhjfoisuju;')
<<<<<<< HEAD
backButton.addEventListener('click', () => {
    location.href = urlIndex
})

applyButton.addEventListener('click', () => {
    let form = document.querySelector('.change-password-form');
    let formData = new FormData(form);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

    if (!csrfToken) {
        message.textContent = 'Ошибка безопасности. Перезагрузите страницу.';
        return;
    }

    // ВАЖНО: Выводим содержимое FormData в консоль для отладки
    for (let pair of formData.entries()) {
        console.log(pair[0]+ ', '+ pair[1]);
    }

    fetch(urlForm, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
        },
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.registered);
            console.log(data.message)
            if (data.reg) {
                alert(data.message);
                message.textContent = data.message
            } else {
                alert(data.message);
                message.textContent = data.message
            }


        })
})
=======
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

>>>>>>> 6595669a3a4a35557f0114ef1d6dcb8b6b1911d8
