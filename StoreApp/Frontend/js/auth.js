let formButton = document.querySelector('#authForm>button');
let form = document.querySelector('#authForm');
let messageError = document.querySelector('#message');

formButton.addEventListener('click', e => {
    let formData = new FormData(form);
    fetch(urlForm, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.reg){
                location.href = urlBase;
            }else {
                messageError.textContent = data.message
            }
        })
        .catch(() => {
           messageError.textContent = 'Ошибка сервера, пожалуйста попробуйте еще раз позднее'
        });
})
