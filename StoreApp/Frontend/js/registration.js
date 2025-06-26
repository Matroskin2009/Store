let formButton = document.querySelector('#registrationForm>button');
let form = document.querySelector('#registrationForm');
let messageError = document.querySelector('.message');

formButton.addEventListener('click', e => {
    e.preventDefault();
    let formData = new FormData(form);
    fetch(urlForm, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrfToken
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
                location.href = urlBase;
            } else {
                messageError.textContent = data.message;
            }
        })
 /*       .catch((e) => {
            messageError.textContent = 'Проверьте все ли впорядке с полями ввода, но возможна и ошибка сервера';
        });
  */
});