from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.crypto import get_random_string


from .models import Url


def inputs(request):
    return render(request, 'shortener/inputs.html')

class InputsView(generic.TemplateView):
    template_name = 'shortener/inputs.html'


def details(request, short_code):
    url = get_object_or_404(Url, short_code=short_code)
    return render(request, 'shortener/details.html', {'url':url })



def post(request):
    try:
        url = Url.objects.get(long_url=request.POST['long_url'])
    except Url.DoesNotExist:
        url = Url()
        url.long_url = request.POST['long_url'] 
        url.short_code = request.POST['short_code']
        url.save()
        return HttpResponseRedirect(reverse('shortener:details', args=(url.short_code, )))


def redirect(request, short_code):
    url = get_object_or_404(Url, short_code=short_code)
    return HttpResponseRedirect(url.long_url)
