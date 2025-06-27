let back_button = document.querySelector('.apply-button')
back_button.addEventListener('click', ()=>{
    location.href = url_index
})

let change_name_button = document.querySelector('#apply-new-name')
change_name_button.addEventListener('click', e => {
    let form = document.querySelector('.change-name-form')
    let form_data = new FormData(form);
    fetch(url_form, {
        method: 'POST',
        body: form_data
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

