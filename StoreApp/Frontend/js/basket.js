document.querySelectorAll('.product-card').forEach(product_card => {
    product_card.addEventListener('click', function (e) {
        e.preventDefault(); // Предотвращаем переход по ссылке
        const product_card_elem = e.target.closest('.product-card');
        const product_id = e.target.getAttribute('data-product-id');
        let quantity = parseInt(e.target.getAttribute('data-quantity'));
        let url_minus = url_minus0.replace('0', product_id);
        let url_plus = url_plus0.replace('0', product_id);
        let url_delete = url_delete0.replace('0', product_id);
        let all_price_element = document.querySelector('.price');
        let all_price = parseInt(all_price_element.textContent.trim()) || 0;

        let fetch_data = function (url_fetch, product_id){
            fetch(url_fetch, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token
                },
                body: JSON.stringify({ 'productId': product_id, 'price': all_price})
            })
                .then(response => response.json())
                .then(data => {
                    if (data.d){
                        product_card_elem.remove();
                        if (document.querySelectorAll('.product-card').length === 0) {
                            document.querySelector('.product-grid').style.display = 'none';
                            document.querySelector('.no-products-two').style.display = 'block';
                        }
                    }
                    document.querySelector('.price').textContent = data.price
                    if (data.success) {
                        product_card_elem.querySelector('.count').textContent = `Количество: ${data.new_quantity}`;
                        product_card_elem.querySelector('.price-cart').textContent = `Цена: ${data.new_price} ₽`;
                        quantity = data.new_quantity;
                        product_card_elem.querySelector('.button-plus').setAttribute('data-quantity', data.new_quantity);
                        product_card_elem.querySelector('.button-minus').setAttribute('data-quantity', data.new_quantity);
                    } else {
                        alert('Ошибка');
                    }
                });
        }

        if (!product_card_elem) return;

        if (e.target.classList.contains('button-plus')) {
            fetch_data(url_plus);
        } else if (e.target.classList.contains('button-minus')) {
            if (quantity > 1) {
                fetch_data(url_minus);
            } else {
                let ask = confirm('Удалить товар из корзины?')
                if (ask){
                    fetch_data(url_delete);
                }
            }
        } else if (e.target.classList.contains('button-delete')){
            let ask = confirm('Удалить товар из корзины?')
            if (ask){
                fetch_data(url_delete);
            }

        } else {
            const base_url = product_card_elem.querySelector('.product-image').dataset.detailUrl.replace('0', product_id);
            window.location.href = base_url;
        }
    });
});