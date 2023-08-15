from .models import FitUser

def authenticate(username, password):
        user = FitUser.objects.get(username=username)
        if user.check_password(password) and user.is_active:
            return user
        return None