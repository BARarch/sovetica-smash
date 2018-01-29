from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.
def index(request):
    #return HttpResponse("Hello Notes")
    template = loader.get_template('index.html')
    rc = RequestContext(request,{'user':request.user})
    rc2 = {'username':'Anthony Quivers'}
    return HttpResponse(template.render(rc2))