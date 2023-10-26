from django.urls import path
from user_profile.views import show_profile
from user_profile.models import Biodata, Wallet

app_name = 'user_profile'

urlpatterns = [
    path('profile/', show_profile, name='show_profile'),

]