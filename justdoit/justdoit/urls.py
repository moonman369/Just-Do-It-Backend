"""
URL configuration for justdoit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import get_tasks_list, get_tasks_by_user, create_or_modify_task, get_task_detail
# from justdoit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', get_tasks_list),
    path('tasks/<slug:user_id>', get_tasks_by_user, name="user_id"),
    path('task-detail/<slug:task_id>', get_task_detail, name="task_id"),
    path('task/<slug:user_id>', create_or_modify_task, name="user_id"),
    path('task/<slug:user_id>', create_or_modify_task, name="user_id"),
    path('task/<slug:user_id>', create_or_modify_task, name="user_id")
]
