let to_basket = document.querySelector('.to-basket');
let basket_form = document.querySelector('.basket-form');
let messages = document.querySelector('.messages');
to_basket.addEventListener('click', (e) => {
    e.preventDefault();

    // Визуальная обратная связь: анимация кнопки
    to_basket.classList.add('clicked');
    const originalText = to_basket.innerHTML;
    setTimeout(() => {
        to_basket.innerHTML = '<span style="vertical-align:middle;">✔ Добавлено!</span>';
    }, 250);
    setTimeout(() => {
        to_basket.classList.remove('clicked');
        to_basket.innerHTML = originalText;
    }, 1200);

    const product_id = basket_form.dataset.productId;
    const base_url = basket_form.action;
    let form_data = new FormData(basket_form);
    fetch(base_url, {
        method: 'POST',
        body: form_data,
    })
        .then(response => response.json())
        .then(response => {
            if (response && response.response) {
                messages.textContent = 'Вы успешно добавили товар!';
                messages.style.color = 'green';
            } else {
                messages.textContent = response.message || 'Ошибка при добавлении товара';
                messages.style.color = 'red';
            }
        })
        .catch(() => {
            messages.textContent = 'Ошибка сети или сервера';
            messages.style.color = 'red';
        });
})
