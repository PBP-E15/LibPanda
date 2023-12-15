from django.urls import path
from user_profile.views import show_profile, edit_biodata, topup_wallet,get_biodata_json,get_wallet_json, get_biodata_flutter, get_wallet_flutter, edit_biodata_flutter, topup_wallet_flutter
from user_profile.models import Biodata, Wallet

app_name = 'user_profile'

urlpatterns = [
    path('profile/', show_profile, name='show_profile'),
    path('edit-biodata/<int:id>', edit_biodata, name='edit_biodata'),
    path('topup-wallet/<int:id>', topup_wallet, name='topup_wallet'),
    path('get-biodata/',get_biodata_json, name='get_biodata_json'),
    path('get-wallet/',get_wallet_json, name='get_wallet_json'),
    path('get-biodata-flutter/<int:id>', get_biodata_flutter, name='get_biodata_flutter'),
    path('get-wallet-flutter/<int:id>', get_wallet_flutter, name='get_wallet_flutter'),
    path('edit-biodata-flutter/<int:id>', edit_biodata_flutter, name='edit_biodata_flutter'),
    path('topup-wallet-flutter/<int:id>', topup_wallet_flutter, name='topup_wallet_flutter'),
]
