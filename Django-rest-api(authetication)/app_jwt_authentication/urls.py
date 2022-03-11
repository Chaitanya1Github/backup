from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from app_jwt_authentication import views

urlpatterns = [
    path('', views.ExampleView.as_view(), name='example_view'),
    path('register/', views.RegisterView.as_view(), name='register_view'),

    # this route generates token.
    # 1. copy the "access" token
    # 2. go to postman, select GET post,
    # 3. in headers enter: key=Authorization, value=copied access token
    # 4. hit enter and you will be able to access the route now
    path('token/generate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # this is to verify if the generated token is valid
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
