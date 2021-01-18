from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user_regular(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile_regular')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users_regular(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator

