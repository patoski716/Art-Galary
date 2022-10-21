from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    posts=Post.objects.order_by('-date_added')
    context={'posts':posts}
    return render(request,'home.html',context)

def PostDetail(request,slug):
    
    post=Post.objects.get(slug=slug)
    commenting= post.commen.all()
# hitcount
    post.blog_views=post.blog_views+1
    post.save()


    new_comment= None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('postdetails',args = [str(post.slug)]))
    else:
        form = CommentForm()
        
    context={'post':post,'form':form,'new_comment':new_comment,'commenting':commenting}
    return render(request, 'details.html',context)

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
  form = PostForm()
  if request.method == 'POST':
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect('dashboard')
  user_contacts = Post.objects.order_by('-date_added').filter(user_id=request.user.id)
  context={'user_contacts': user_contacts,'form':form}
  return render(request,'dashboard.html',context)


def search(request):
  posts = Post.objects.order_by('-date_added')
  if 'title' in request.GET:
      title = request.GET['title']
      if title:
          query = Post.objects.filter(title__icontains=title)
          
  context={'query':query,'posts':posts}
  return render(request,'search.html',context)