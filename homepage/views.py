from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone



class HomepageView(generic.ListView):
    template_name = 'homepage/homepage.html'

    # In case we define a comportment in the homepage linked with a DATABASE we have to set this function
    def get_queryset(self):
        """

        """
        return

