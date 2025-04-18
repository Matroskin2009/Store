let formButton = document.querySelector('#registrationForm>button');
let form = document.querySelector('#registrationForm');
let messageError = document.querySelector('.message');

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
            alert('ошибка сервера, пожалуйста попробуйте повторить попытку позднее...')
            message.textContent = 'Ошибка на стороне серве, пожалуйста повторите попытку позднее';
        });
})