from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('public/', views.public_api),
    path('protected/', views.protected_api),
    path('login/', obtain_auth_token),
    path('send-email/', views.trigger_email),
    path('test-email/', views.test_email),

]