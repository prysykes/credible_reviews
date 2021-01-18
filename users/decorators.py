from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user_regular(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile_regular')
        else:
            # send a warning for annonymous and company users
            
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users_regular(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            #checks to see if the user belongs to a group before returning the view_func
            if not request.user.groups.filter(name__in=['company']).exists():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/')
        return wrapper_func
    return decorator

