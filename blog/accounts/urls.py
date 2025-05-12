from django.urls import path
from .views import reg_log_view


urlpatterns = [
    path('auth/', reg_log_view, name='reg_log')
]