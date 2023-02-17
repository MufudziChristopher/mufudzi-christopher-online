from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
# Create your views here.
def home(request):

    context = {}
    return render(request, 'home/index.html', context)

def idaca(request):

        return render(request, 'home/idaca.html', {})

def gallery(request):

    return render(request, 'home/gallery.html', {})




def bc(request):

    return render(request, 'home/bc.html', {})




def africanus(request):

    return render(request, 'home/africanus.html', {})


def about(request):

    return render(request, 'home/about.html', {})

def services(request):

    return render(request, 'home/services.html', {})

def contact(request):

    return render(request, 'home/contact.html', {})
