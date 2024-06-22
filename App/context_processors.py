from .models import AvatarUsuario

def avatar_usuario(request):
    avatar = None
    if request.user.is_authenticated:
        avatar = AvatarUsuario.objects.filter(usuario=request.user).first()
    return {'avatar': avatar}