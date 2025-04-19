let backButton = document.querySelector('.apply-button')
let applyButton = document.querySelector('#apply-new-password')
let message = document.querySelector('.message')
alert('isdhjfoisuju;')

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
            if (data.reg) {
                alert(data.message);
                message.textContent = data.message
            } else {
                alert(data.message);
                message.textContent = data.message
            }

        })
})
