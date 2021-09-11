from django.urls import path
from . import views

urlpatterns = [
    path('', views.details, name='details'),
    path('add-mark', views.addMark, name='addMark'),
    path('result', views.result, name='result'),
    path('<int:id>', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
]