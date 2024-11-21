from django.shortcuts import render,redirect
from  greenrootapp.models import users
from  greenrootapp.models import post,comment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method=="POST":
          
        title=request.POST.get("title")
        content=request.POST.get("content")

        posts=post.objects.create(title=title,problem=content)
        posts.save()
        return redirect(register)
        
    return render(request,"index.html")


def register(request):
     if request.method=="POST":
          
       username=request.POST.get("username")
       email=request.POST.get("email")
       password=request.POST.get("password")
       confirmpassword=request.POST.get("confirmpassword")

       user=users.objects.create_user(username=username,email=email,password=password)
       
       user.save()
       return redirect(Login)
     return render(request,"signup.html")


def Login(request):
     if request.method=="POST":
         
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(dashboard)
     return render(request,"login.html")
@login_required
def dashboard(request):
     posts=post.objects.all()
     # id=post.objects.filter(id=)
     return render(request,"Questions321.html",{"posts": posts})


@login_required
def posts(request):
    
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get("content")

        posts=post.objects.create(title=title,problem=content,user=request.user)
        posts.save()
        return redirect(dashboard)
        
    return render(request,"Questions3.html")
@login_required
def problem(request,pk):
    
    posts=post.objects.filter(id=pk)
    comments=comment.objects.filter(post_id=pk)
   # comments_user=comment.objects.filter(user_id=pk,)
    
    link={
        "post":posts,
        "comment":comments,
        "pk":pk
        #"comments_user": comments_user
    }
    if request.method=="POST":
        
       enter_answer=request.POST.get("enter_answer")
       your_answer=comment.objects.create(answer=enter_answer,user=request.user,post_id=pk)
       your_answer.save()
       return redirect(dashboard)
    return render(request,"shareanswers.html", link)

def Logout(request):
    logout(request)
    return redirect(Login)
# Create your views here.
