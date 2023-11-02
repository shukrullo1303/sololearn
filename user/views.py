from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import  SignUpForm, MyUserChangeForm
from django.contrib import messages
from course.models import Course, PageOfCourse, Quiz, Choice, Lesson
from .models import User


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            user = form.save()       
            login(request, user)
            messages.success(request, "Registratsiyadan muvaffaqqiyatli o\'tdingiz." )
            return redirect('home')
        else:
            messages.error(request, "Registratsiyadan o\'tish amalga oshmadi. Ma\'lumotlar xato emasligini tekshiring.")
            return redirect("register")
    form = SignUpForm()
    context = {
        'form': form
     }
    return render(request, 'register.html', context)


def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:    
            login(request, user)
            messages.success(request, (f"{username} akkauntingizga muvaffaqqiyatli kirdingiz"))
            return redirect('home')
        else:
            messages.success(request, ("Xatolik! Parol yoki username xato."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "akkauntingizdan muvaffaqqiyatli chiqib ketdingiz.") 
        return redirect('home')
    else: 
        messages.info(request, "Ro'yxatdan o'tmagansiz!") 
        return redirect(request.META.get('HTTP_REFERER'))


def home(request):
    active_courses = Course.objects.filter(active=request.user.id)
    courses = Course.objects.all()
    context = {
        'courses': courses,
        "active_courses": active_courses,
    }
    return render(request, "home.html", context)


def profile(request, pk):
    if request.user.is_authenticated:
        user_profile = User.objects.get(id=pk)
        active_courses = Course.objects.filter(active=user_profile.id)
        context = {
            "user_profile": user_profile,
            "active_courses": active_courses,
        }
        return render(request, "profile.html", context)
    else: 
        return redirect("register")


def leaderboard(request):
    users = User.objects.all().order_by("-xp")
    context = {
        "users": users 
    }
    return  render(request, "leaderboard.html", context)



def upload_picture_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = MyUserChangeForm(request.POST or None, request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("Profilingiz ma'lumotlari yangilandi"))
            return redirect('home')

        return render(request, 'picture.html', {'form': form})
    else:
        messages.success(request, ("Ushbu sahifani ko\'rish uchun ro\'yxatdan o\'tgan bo\'lishingiz shart!" ))
        return redirect('home')