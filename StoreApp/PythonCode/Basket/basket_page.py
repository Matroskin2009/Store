import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from StoreApp.models import Product, CartItem

class ButtonsBasket:
    @staticmethod
    @csrf_exempt
    def button_minus(request, product_id):
        d = None
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Метод не разрешен'}, status=405)

        try:
            data = json.loads(request.body)
            price = int(data.get('price'))
            product = get_object_or_404(Product, id=product_id)
            # Ищем товар в корзине текущего пользователя
            item = get_object_or_404(CartItem, user=request.user, product=product)
            price = price - product.price

            if item.quantity > 1:
                item.quantity -= 1
                item.save()
                d = False
                message = f'Количество уменьшено до {item.quantity}'
            else:
                item.delete()
                d = True
                message = 'Товар удален из корзины'

            return JsonResponse({
                'success': True,
                'message': message,
                'new_quantity': item.quantity,
                'new_price': product.price * item.quantity,
                'price': price
            })

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e), 'product_id': product_id, 'd': d}, status=400)

    @staticmethod
    def button_plus(request, product_id):
        try:
            data = json.loads(request.body)
            price = int(data.get('price'))
            product = get_object_or_404(Product, id=product_id)
            item = get_object_or_404(CartItem, user=request.user, product=product)
            item.quantity += 1
            price = price + product.price
            item.save()

            return JsonResponse({
                'success': True,
                'new_quantity': item.quantity,
                'new_price': product.price * item.quantity,
                'price': price
            })

        except Exception as e:
            print(f'Ошибка {e}')
            return JsonResponse({'success': False}, status=400)

    @staticmethod
    def button_delete(request, product_id):
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Метод не разрешен'}, status=405)
        try:
            product = get_object_or_404(Product, id=product_id)
            data = json.loads(request.body)
            price = int(data.get('price'))
            item = get_object_or_404(CartItem, user=request.user, product=product)
            price = price - product.price * item.quantity
            item.delete()

            return JsonResponse({'success': True, 'd': True, 'price': price})

        except Exception as e:
            return JsonResponse({'success': False}, status=400)

class BasketPage:
    def to_basket(request):
        user_id = request.session.get('user_id')
        cart_items = CartItem.objects.filter(user=request.user).select_related('product')
        total_price = 0
        products_in_cart = []

        for item in cart_items:
            product = item.product
            product.quantity = item.quantity
            product.carts_price = product.price * product.quantity
            total_price += product.carts_price
            products_in_cart.append(product)

        context = {
            'products': products_in_cart,
            'total_price': total_price,
            'response': True,
            'user_id': user_id
        }
        return render(request, 'basket.html', context)