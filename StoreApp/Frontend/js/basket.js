document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('click', function (e) {
        e.preventDefault(); // Предотвращаем переход по ссылке
        const productCard = e.target.closest('.product-card');
        const productId = e.target.getAttribute('data-product-id');
        let quantity = parseInt(e.target.getAttribute('data-quantity'));
        let urlMinus = urlMinus0.replace('0', productId);
        let urlPlus = urlPlus0.replace('0', productId);
        let urlDelete = urlDelete0.replace('0', productId);
        let allPriceElement = document.querySelector('.price');
        let allPrice = allPriceElement.textContent.trim();

        let Fetch = function (urlFetch, productId){
            fetch(urlFetch, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ 'productId': productId, 'price': allPrice})
            })
                .then(response => response.json())
                .then(data => {
                    if (data.d){
                        productCard.remove();
                        if (document.querySelectorAll('.product-card').length === 0) {
                            document.querySelector('.product-grid').style.display = 'none';
                            document.querySelector('.no-products-two').style.display = 'block';
                        }
                    }
                    document.querySelector('.price').textContent = data.price
                    if (data.success) {
                        productCard.querySelector('.count').textContent = `Количество: ${data.newQuantity}`;
                        productCard.querySelector('.price-cart').textContent = `Цена: ${data.newPrice} ₽`;
                        quantity = data.newQuantity;
                        productCard.querySelector('.button-plus').setAttribute('data-quantity', data.newQuantity);
                        productCard.querySelector('.button-minus').setAttribute('data-quantity', data.newQuantity);
                    } else {
                        alert('Ошибка');
                    }
                });
        }

        if (!productCard) return;

        if (e.target.classList.contains('button-plus')) {
            Fetch(urlPlus);
        } else if (e.target.classList.contains('button-minus')) {
            if (quantity > 1) {
                Fetch(urlMinus);
            } else {
                let ask = confirm('Удалить товар из корзины?')
                if (ask){
                    Fetch(urlDelete);
                }
            }
        } else if (e.target.classList.contains('button-delete')){
            let ask = confirm('Удалить товар из корзины?')
            if (ask){
                Fetch(urlDelete);
            }

        } else {
            const baseUrl = productCard.querySelector('.product-image').dataset.detailUrl.replace('0', productId);
            window.location.href = baseUrl;
        }
    });
});