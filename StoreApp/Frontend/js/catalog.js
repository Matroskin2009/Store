let toBasket = document.querySelector('.to-basket');
let basketForm = document.querySelector('.basket-form');
let messages = document.querySelector('.messages');
toBasket.addEventListener('click', (e) => {
    e.preventDefault(); // Предотвращаем отправку формы по умолчанию

    const productId = basketForm.dataset.productId;
    const baseUrl = basketForm.action;  // Берем URL из атрибута action формы
    let formData = new FormData(basketForm);
    fetch(baseUrl, {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(response => {
            if (response) {
                messages.textContent = 'Вы успешно добавили товар!';
                messages.style.color = 'green';
            } else {
                messageError.textContent = response.message;
            }
        })
})
