from django.shortcuts import render, redirect
from .models import Blog, Bloglist
from django.shortcuts import render, get_object_or_404
from .models import Packages, Bloglist, Blog, Lead, AdminDashboardProfile

def package_list(request):
    home_packages = Packages.objects.filter(category='home')
    business_packages = Packages.objects.filter(category='business')
    
    if request.method == "POST":
        Lead.objects.create(
            full_name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        return redirect('package_list')
        
    return render(request, 'packages.html', {
        'home_packages': home_packages,
        'business_packages': business_packages
    })

def blog_list_view(request):
    items = Bloglist.objects.all().order_by('-date')
    return render(request, 'blog_list.html', {'items': items})

def blog_detail_view(request, pk):
    post = get_object_or_404(Blog, blog_list_ref_id=pk)
    return render(request, 'blog_detail_view.html', {'post': post})

def index(request):
    if request.method == "POST":
        Lead.objects.create(
            full_name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        return redirect('my_index')
    return render(request, 'index.html')

def admin_profile(request):
    profile = get_object_or_404(AdminDashboardProfile, user=request.user)
    return render(request, 'admin_profile.html', {'profile': profile})



