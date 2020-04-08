from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication import views as authentication_views



urlpatterns = [
    path('user/create/',
         authentication_views.CustomUserCreate.as_view(),
         name="create_user"),
    path('token/obtain/',
         authentication_views.CustomTokenPairView.as_view(),
         name='token_create'),  # override sjwt stock token
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]

urlpatterns += [
    path('hello/',
         authentication_views.HelloWorldView.as_view(),
         name='hello_world')
]
