from django.urls import path
from playground.views import say_hello, index

urlpatterns = [
    path('', say_hello),
    path('index/', index)
]