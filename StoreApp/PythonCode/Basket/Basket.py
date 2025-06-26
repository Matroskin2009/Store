import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from StoreApp.models import Product, CartItem

class ButtonsBasket:
    @staticmethod
    @csrf_exempt
    def buttonMinus(request, productId):
        d = None
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Метод не разрешен'}, status=405)

        try:
            data = json.loads(request.body)
            price = int(data.get('price'))
            product = get_object_or_404(Product, id=productId)
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
                'newQuantity': item.quantity,
                'newPrice': product.price * item.quantity,
                'price': price
            })

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e), 'productId': productId, 'd': d}, status=400)

    @staticmethod
    def buttonPlus(request, productId):
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Метод не разрешен'}, status=405)
        try:
            data = json.loads(request.body)
            price = int(data.get('price'))
            data = json.loads(request.body)
            price = int(data.get('price'))
            product = get_object_or_404(Product, id=productId)
            item = get_object_or_404(CartItem, user=request.user, product=product)
            item.quantity += 1
            price = price + product.price
            item.save()

            return JsonResponse({
                'success': True,
                'newQuantity': item.quantity,
                'newPrice': product.price * item.quantity,
                'price': price
            })

        except Exception as e:
            print(f'Ошибка {e}')
            return JsonResponse({'success': False}, status=400)

    @staticmethod
    def buttonDelete(request, productId):
        if request.method != 'POST':
            return JsonResponse({'success': False, 'message': 'Метод не разрешен'}, status=405)
        try:
            product = get_object_or_404(Product, id=productId)
            data = json.loads(request.body)
            price = int(data.get('price'))
            item = get_object_or_404(CartItem, user=request.user, product=product)
            price = price - product.price * item.quantity
            item.delete()

            return JsonResponse({'success': True, 'd': True, 'price': price})

        except Exception as e:
            return JsonResponse({'success': False}, status=400)

class BasketPage:
    def toBasket(request):
        user_id = request.session.get('user_id')
        cartItems = CartItem.objects.filter(user=request.user).select_related('product')
        totalPrice = 0
        productsInCart = []

        for item in cartItems:
            product = item.product
            product.quantity = item.quantity
            product.cartsPrice = product.price * product.quantity
            totalPrice += product.cartsPrice
            productsInCart.append(product)

        context = {
            'products': productsInCart,
            'totalPrice': totalPrice,
            'response': True,
            'user_id': user_id
        }
        return render(request, 'basket.html', context)