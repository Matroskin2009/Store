let form_button = document.querySelector('#authForm>button');
let form = document.querySelector('#authForm');
let message_error = document.querySelector('#message');

form_button.addEventListener('click', e => {
    let form_data = new FormData(form);
    fetch(url_form, {
        method: 'POST',
        body: form_data
    })
        .then(response => response.json())
        .then(data => {
            if (data.reg){
                location.href = url_base;
            }else {
                message_error.textContent = data.message
            }
        })
        .catch(() => {
           message_error.textContent = 'Ошибка сервера, пожалуйста попробуйте еще раз позднее'
        });
})
