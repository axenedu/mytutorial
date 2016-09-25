
from django.shortcuts import render
from django.views import View

# Create your views here.

class LandingView(View):
    template_name = 'base/index.html'

    def get(self, request):
        return render(request, self.template_name)