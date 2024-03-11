from django.urls import path
from .views import users_list, users_detail

urlpatterns = [
    path('all/', users_list, name="users_page"),
    path('detail/<int:id>', users_detail, name="user_detail"),

]
