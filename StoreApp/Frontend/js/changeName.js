let backButton = document.querySelector('.apply-button')
backButton.addEventListener('click', ()=>{
    location.href = urlIndex
})

let changeNameButton = document.querySelector('#apply-new-name')
changeNameButton.addEventListener('click', e => {
    let form = document.querySelector('.change-name-form')
    let formData = new FormData(form);
    fetch(urlForm, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.reg){
                location.reload()
                alert('успешно!');
            }else {
                alert("ошибка!")
            }
        })
        .catch(() => {
            alert('ошибка сервера, пожалуйста попробуйте повторить попытку позднее...')
        });
})

