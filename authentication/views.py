from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import Biodata, Wallet
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "password": request.POST['password'],
                "wallet_pk": user.wallet.id,
                "biodata_pk": user.biodata.id,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username=username, password=password)

        name = new_user.username
        email = "no_email@email.com"
        gender = ""
        birthday = "2004-05-04"
        phone_number = "040504"

        new_biodata = Biodata(user=new_user, name=name, email=email, gender=gender, birthday=birthday, phone_number=phone_number)
        new_biodata.save()

        balance = 0
        new_wallet = Wallet(user=new_user, balance=balance)
        new_wallet.save()


    return JsonResponse({
            "status": True,
            "message": "Account created successfully!",
            "user_id": new_user.id,
        }, status=200)
    
    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)
