from django.shortcuts import render,HttpResponseRedirect
from .forms import signupForm,LoginForm,Postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.
#home
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'post':posts})
#about
def about(request):
    return render(request,'blog/about.html')
#contact
def contact(request):
    return render(request,'blog/contact.html')
#dashboard
def dash(request):
    if request.user.is_authenticated:
        post=Post.objects.all()
        user=request.user
        name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'blog/dashboard.html',{'post':post,"name":name,"gp":gps})
    else:
        return HttpResponseRedirect('/login/')
#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
#signup
def user_signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations!!! you become author')
            user=form.save()
    else:
        form=signupForm()
    return render(request,'blog/signup.html',{'form':form})
#login
def user_login(request):
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form})
#Add new Post
def edit_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=Postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=Postform(instance=pi)
        return render(request,'blog/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
#Add new Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=Postform(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                des=form.cleaned_data['des']
                pst=Post(title=title,des=des)
                pst.save()
                form=Postform()
        else:
            form=Postform()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
#Add new Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')