from django.urls import path


from .views import *

urlpatterns = [
    path('', (TextBoard.as_view()), name='new_list'),
]
