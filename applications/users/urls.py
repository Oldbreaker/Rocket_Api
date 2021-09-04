from django.urls import path
from . import views


urlpatterns = [
    # url para crear usuario
    path('users/create', views.CreateUser.as_view(),),
    # url para regresar un usuario por pk
    path('users/get/<int:pk>', views.RetrieveUser.as_view()),
    path('users/delete/<int:pk>', views.DestroyUser.as_view()),
    path('users/update/<int:pk>', views.UpdateUser.as_view()),
]
