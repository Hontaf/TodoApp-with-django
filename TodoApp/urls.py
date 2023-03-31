"""TodoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoList import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.todo_home,name='home'),
    path('todo-detail/<int:id>/',views.todo_detail,name="detail"),
    path('todo_create/',views.todo_create,name='create'),
    path('todo_update/<int:id>/',views.todo_update,name='update'),
    path('todo_delete/<int:id>/',views.todo_delete,name='delete')
]