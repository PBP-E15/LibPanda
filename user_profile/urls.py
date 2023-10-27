from django.urls import path
from user_profile.views import show_profile, edit_biodata, topup_wallet,get_biodata_json,get_wallet_json
from user_profile.models import Biodata, Wallet

app_name = 'user_profile'

urlpatterns = [
    path('profile/', show_profile, name='show_profile'),
    path('edit-biodata/<int:id>', edit_biodata, name='edit_biodata'),
    path('topup-wallet/<int:id>', topup_wallet, name='topup_wallet'),
    path('get-biodata/',get_biodata_json, name='get_biodata_json'),
    path('get-wallet/',get_wallet_json, name='get_wallet_json'),
]
