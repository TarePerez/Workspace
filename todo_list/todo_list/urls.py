"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from tasks.views import task_list, create_task, update_task, delete_task, reset_tasks

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('reset-tasks/', reset_tasks, name='reset_tasks'),
]
