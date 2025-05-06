from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
import logging

from django.views.decorators.csrf import csrf_exempt

from StoreApp.models import User, Product, Category, SubCategory

logger = logging.getLogger(__name__)

def Index(request):
    subcategories = SubCategory.objects.filter(products__isnull=False).distinct()
    categories = Category.objects.filter(products__isnull=False).distinct()
    user_id = request.session.get('user_id')

    if user_id:
        return render(request, 'index.html', context={'userRegistered': True, 'categories': categories, 'subcategories': subcategories})
    else:
        return render(request, 'index.html', context={'userRegistered': False, 'categories': categories, 'subcategory': subcategories})

def basket(request):
    return render(request, 'basket.html')

def account(request):
    orderCount = 0
    username = request.session.get('username')
    return render(request, 'account.html', context={'name': username, 'orderCount': orderCount})

def liked(request):
    return render(request, 'liked.html')


def productList(request):
    # Получаем параметры
    # get params
    user_id = request.session.get('user_id')
    subcategory_id = request.GET.get('subcategory')
    category_id = request.GET.get('category')
    category_id = request.GET.get('category_id')
    search_query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort', 'id')

    # QuerySet создается тут
    # The QuerySet is created here
    products = Product.objects.all()


    if category_id:
        products = products.filter(category_id=category_id)

    # Фильтрация
    # Filtering
    if subcategory_id:
        products = products.filter(subcategory_id=subcategory_id)

    if search_query:
        products = products.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if min_price:
        min_price = float(min_price)
        products = products.filter(price__gte=min_price)
    if max_price:
        max_price = float(max_price)
        products = products.filter(price__lte=max_price)


    # Сортировка
    #sorting
    sorting_options = {
        'price_asc': ['price'],
        'price_desc': ['-price'],
        'id': ['id']
    }
    products = products.order_by(*sorting_options.get(sort, ['id']))

    # Пагинация
    # pagination
    paginator = Paginator(products, 21)
    page_obj = paginator.get_page(request.GET.get('page', 1))

    #использовал другой подход к user_id по причине грамозкости conext
    # i used another way to the user_id because context is very big
    context = {
        'products': page_obj,
        'filtered_count': paginator.count,
        'search_query': search_query,
        'price_range': {
            'min': min_price if isinstance(min_price, float) else None,
            'max': max_price if isinstance(max_price, float) else None
        },
        'current_subcategory': subcategory_id,
        'category_id': category_id,
        'current_sort': sort,
        'user_id': user_id
    }
    return render(request, 'productList.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_id = request.session.get('user_id')
    if user_id:
        return render(request, 'catalog.html', context={'product': product, 'userRegistered': True})
    else:
        return render(request, 'catalog.html', context={'product': product, 'userRegistered': False})
