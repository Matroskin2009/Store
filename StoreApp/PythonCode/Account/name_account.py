from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from StoreApp.models import User
import logging
logger = logging.getLogger(__name__)

class NameAccount:
    @staticmethod
    def change_name_form(request):
        if 'user_id' in request.session:
            username = request.session.get('username')
            return render(request, 'change_name.html', context={'name': username})
        else:
            return render(request, 'index.html', context={'registered': False})

    @staticmethod
    @csrf_exempt
    def change_name(request):
        if request.method == 'POST':
            new_username = request.POST.get('new_name')
            if 'user_id' in request.session:
                try:
                    if User.objects.filter(username=new_username).exists():
                        logger.error('Пользователь уже создан, ошибка.')
                        return JsonResponse({'reg': False, 'message': 'пользователь был зарегистрирован ранее', 'name': new_username}, status=409)
                    if new_username:
                        if new_username != request.session['username']:
                            user = User.objects.get(id=request.session['user_id'])
                            user.username = new_username
                            user.save()
                            request.session['username'] = new_username
                            return JsonResponse({'reg': True, 'message': 'Вы успешно поменяли имя!', 'name': new_username}, status=200)
                        else:
                            return JsonResponse({'reg': False, 'message': 'Прошлое имя должно отличаться от старого!', 'name': new_username}, status=400)
                    else:
                        return JsonResponse({'reg': False, 'message': 'Имя не может быть пустым!', 'name': new_username}, status=400)
                except Exception as e:
                    return JsonResponse({'reg': False, 'message': f'Ошибка сервера, попробуйте позже: {e}', 'name': new_username}, status=500)
            else:
                return JsonResponse({'reg': False, 'registered': False})
        else:
            username = request.session.get('username')
            return render(request, 'change_name.html', context={'name': username})