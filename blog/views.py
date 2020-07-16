from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost, Contact

# Create your views here.


def index(request):
    categoryProds = BlogPost.objects.all()
    n = len(categoryProds)
    params = {'blogPosts': categoryProds, 'range': range(1, n)}
    return render(request, 'blog/index.html', params)

def blogpost(request,myid):
    post = BlogPost.objects.filter(id=myid)[0]
    try:
        next = BlogPost.objects.filter(id=myid+1)[0]
        prev = BlogPost.objects.filter(id=myid-1)[0]
        print(next, prev)
        params = {'post': post, 'prev':prev, 'next': next}
    except IndexError:
        pass
    params = {'post': post}
    return render(request, 'blog/blogpost.html', params)

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        return render(request, 'blog/contact.html', {'thank':thank})
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'shop/about.html')

