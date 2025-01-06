from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserSerializer

# Create your views here.

## API views.
class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request):
        user = request.user
        data = request.data
        profile = user.profile
        profile.phone_number = data.get('phone_number', profile.phone_number)
        profile.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


## Web views.
@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile  # Obtener el perfil extendido del usuario.

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()

        # Actualizar datos del usuario.
        user.username = username
        user.email = email
        if password:  # Solo actualiza la contraseña si el campo no está vacío.
            user.set_password(password)
            update_session_auth_hash(request, user)  # Mantener la sesión activa después de cambiar la contraseña.
        user.save()

        profile.phone_number = phone_number
        profile.save()

        messages.success(request, '¡Tu perfil se ha actualizado correctamente!')
        return redirect('edit-profile')

    return render(request, 'authentication/edit_profile.html', {'user': user})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()

        # Validar que el usuario o el email no existan.
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return render(request, 'authentication/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado.')
            return render(request, 'authentication/register.html')

        # Crear usuario (el perfil se crea automáticamente por la señal)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.profile.phone_number = phone_number
        user.profile.save()
        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('login')
    return render(request, 'authentication/register.html')



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        try:
            # Busca el usuario por correo electrónico.
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Correo electrónico no registrado.')
            return render(request, 'authentication/login.html')

        # Autentica al usuario usando el username asociado al email.
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('edit-profile')
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')

    return render(request, 'authentication/login.html')
