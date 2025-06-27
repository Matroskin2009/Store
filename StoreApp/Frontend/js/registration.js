let form_button = document.querySelector('#registrationForm>button');
let form = document.querySelector('#registrationForm');
let message_error = document.querySelector('.message');

form_button.addEventListener('click', e => {
    e.preventDefault();
    let form_data = new FormData(form);
    fetch(url_form, {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.reg) {
                location.href = url_base;
            } else {
                message_error.textContent = data.message;
            }
        })
});