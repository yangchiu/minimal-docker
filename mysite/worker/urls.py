from django.urls import path

from . import views

app_name = 'worker'
urlpatterns = [
    # /polls/
    path('enqueue/<int:number>/', views.enqueue, name='enqueue'),
    # /polls/5/
    path('list', views.list, name='list'),
]
