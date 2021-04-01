from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone



# Generic View Index ( a view called from a class where we define a template_name then call it in a root patterns )

class RegistrationView(generic.ListView):
    template_name = 'registration/login.html'


    def get_queryset(self):
        """

        """
        return
