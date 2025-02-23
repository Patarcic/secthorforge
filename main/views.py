from django.shortcuts import render
from django.utils.translation import gettext as _  # Import translation function

def home(request):
    message = _("Welcome to Secthor Forge!")  # This is a translatable string
    return render(request, 'main/home.html', {"message": message})
