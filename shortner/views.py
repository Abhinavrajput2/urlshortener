from django.shortcuts import render
import uuid
from .models import URL
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import URL


# Create your views here.
def index(request):
    return render(request, 'index.html')



def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:3]
        new_url = URL(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)  # Just return the code, no text prefix

def go(request, pk):
    url = get_object_or_404(URL, uuid=pk)
    return redirect(url.link)


   