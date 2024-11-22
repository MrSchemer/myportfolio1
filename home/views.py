from django.shortcuts import render, HttpResponse
from .models import Portfolio, Blog, Contact

from datetime import datetime

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('message')  
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            desc=desc,
            date=datetime.now()
        )
        contact.save()
        
        return HttpResponse("Thank you for your message!")
    return render(request, 'home/home.html')


def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-date').filter(catagory='project')
    return render(request, 'home/portfolio.html', {'portfolios': portfolios})



def blog(request):
    posts = Blog.objects.all()
    return render(request, 'home/blog.html', {'posts': posts})


def blogpost(request, slug):
    post= Blog.objects.filter(slug=slug).first()
    print(post.desc)
    return render(request, 'home/blogpost.html', {'post': post})
