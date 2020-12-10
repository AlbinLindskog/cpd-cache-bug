from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('', lambda *args, **kwargs: HttpResponse('The status should be 403',  status=403))
]
