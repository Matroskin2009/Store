let back_button = document.querySelector('.apply-button')
let apply_button = document.querySelector('#apply-new-password')
let message = document.querySelector('.message')


back_button.addEventListener('click', () => {
    location.href = url_index
})

apply_button.addEventListener('click', () => {
    let form = document.querySelector('.change-password-form');
    let form_data = new FormData(form);
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

    if (!csrf_token) {
        message.textContent = 'Ошибка безопасности. Перезагрузите страницу.';
        return;
    }

    fetch(url_form, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: form_data
    })
        .then(response => response.json())
        .then(data => {
            if (data.reg) {
                alert(data.message);
            } else {
                alert(data.message);
                message.textContent = data.message
            }
        })
})
