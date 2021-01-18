from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user_company(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('company_users/profile_company')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users_company(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)
            
        return wrapper_func
    return decorator