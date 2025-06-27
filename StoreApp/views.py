from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import logging
from StoreApp.models import Product, Category, SubCategory, CartItem
logger = logging.getLogger(__name__)
# The main page
def index(request):
    subcategories = SubCategory.objects.filter(products__isnull=False).distinct()
    categories = Category.objects.filter(products__isnull=False).distinct()
    user_id = request.session.get('user_id')
    return render(request, 'index.html', context={'user_id': user_id, 'categories': categories, 'subcategories': subcategories})

# Redirects and displays the name and number of orders for this user
def account(request):
    order_count = 0
    username = request.session.get('username')
    return render(request, 'account.html', context={'name': username, 'order_count': order_count})

# The list of products with sorting functionality
def product_list(request):
    user_id = request.session.get('user_id')

    search_query = request.GET.get('q')
    search_ids_str = request.GET.get('search_result_ids')
    category_id = request.GET.get('category_id')
    subcategory_id = request.GET.get('subcategory')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort', 'id')

    products = Product.objects.all()
    search_ids = None

    # Обработка поиска
    if search_query:
        # Если есть поисковый запрос, ищем по нему
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )
        search_ids = list(products.values_list('id', flat=True))
    elif search_ids_str and search_ids_str.strip() and search_ids_str != 'None':
        # Если есть сохраненные ID из предыдущего поиска
        try:
            ids_list = [int(id_str) for id_str in search_ids_str.split(',') if id_str.strip()]
            if ids_list:  # Проверяем, что список не пустой
                products = products.filter(id__in=ids_list)
                search_ids = ids_list
            else:
                # Если список пустой, не показываем ничего
                products = Product.objects.none()
        except ValueError:
            # Если ошибка в парсинге ID, не показываем ничего
            products = Product.objects.none()

    # Применяем остальные фильтры
    if category_id:
        products = products.filter(category_id=category_id)
    if subcategory_id:
        products = products.filter(subcategory_id=subcategory_id)

    # Фильтрация по цене
    try:
        if min_price:
            min_price_val = float(min_price)
            products = products.filter(price__gte=min_price_val)
    except ValueError:
        min_price_val = None

    try:
        if max_price:
            max_price_val = float(max_price)
            products = products.filter(price__lte=max_price_val)
    except ValueError:
        max_price_val = None

    # Сортировка
    sorting_options = {
        'price_asc': ['price'],
        'price_desc': ['-price'],
        'id': ['id']
    }
    products = products.order_by(*sorting_options.get(sort, ['id']))

    context = {
        'user_id': user_id,
        'products': products,
        'current_sort': sort,
        'search_query': search_query,
        'search_result_ids': ','.join(map(str, search_ids)) if search_ids else None,
        'price_range': {
            'min': min_price_val if 'min_price_val' in locals() else None,
            'max': max_price_val if 'max_price_val' in locals() else None
        },
        'category_id': category_id,
        'current_subcategory': subcategory_id,
    }

    return render(request, 'product_list.html', context)

# Product review page
def product_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_id = request.session.get('user_id')
    return render(request, 'product_page.html', context={'product': product, 'user_id': user_id})

def product_page3d(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.model_3d:
        product_model3d = product.model_3d
    else:
        product_model3d = None
    user_id = request.session.get('user_id')
    return render(request, 'product_page3d.html', context={'product': product, 'user_id': user_id, 'model3d': product_model3d})

# Add to basket
def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        item.quantity += 1
        item.save()


    return JsonResponse({'response': True, 'total_price': total_price})
