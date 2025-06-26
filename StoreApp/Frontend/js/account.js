let form = document.querySelector('#form');
let exitButton = document.querySelector('.Exit');

exitButton.addEventListener('click', (e) => {
    let check = prompt(
        'Убедитесь, что вы сохранили данные аккаунта, в противном случае вы можете их потерять. Для выхода напишите "ВЫХОД"'
    );
    if (check !== null) {
        check = check.toLowerCase();
        if (check === "выход") {
            fetch(urlForm, {
                method: 'POST',
                body: null,
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(data.message);
                        location.href = urlReg;
                    } else {
                        alert('Ошибка: ' + (data.message || 'неизвестная ошибка'));
                    }
                })
                .catch(()=> {
                    alert("Ошибка на стороне сервера, пожалуйста попробуйте позднее");
                });
        } else {
            alert('вы неправильно написали слово "ВЫХОД"');
        }
    } else {
        alert('Вы отменили выход');
    }
});






