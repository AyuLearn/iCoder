from django.shortcuts import render, redirect
from .models import Contact, Post, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    recents = Post.objects.order_by('-dt')[0:3]
    paginator = Paginator(posts, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'recents': recents
    }
    return render(request, 'blog.html', context)

def post(request, slug):
    latests = Post.objects.order_by('-dt')[0:3]
    post = Post.objects.filter(slug=slug).first()
    comments = Comments.objects.all().filter(post=post)
    context = {
        'latests': latests,
        'post': post,
        'comments': comments
    }
    return render(request, 'post.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def postComments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        user = request.user
        post = Post.objects.get(sno=postSno)

        comments = Comments(comment=comment, user=user, post=post)
        comments.save()
    return redirect(f"/{post.slug}")

def signupUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('blog')
    return render(request, 'signup.html')

def loginUser(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            return redirect('blog')
        else:
            return redirect('blog')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('blog')