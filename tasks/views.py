from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Project
from .forms import SignUpForm, TaskForm

# Check if the user is an admin
def is_admin(user):
    return user.is_superuser

# Landing Page
def home(request):
    return render(request, 'tasks/home.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully! 🎉")
            return redirect('task_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, 'tasks/signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! ✅")
            return redirect("task_list")
        else:
            messages.error(request, "Invalid username or password. ❌")
    return render(request, "tasks/login.html")

# Logout View
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out. 👋")
    return redirect("login")

# View Tasks - Standard User & Admin
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Create Task - Any Logged-in User
@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task created successfully! 📌")
            return redirect('task_list')
        else:
            messages.error(request, "Error creating task. Please try again.")
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Update Task - Admin Only
@login_required
@user_passes_test(is_admin)
def update_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully! ✏️")
            return redirect('task_list')
        else:
            messages.error(request, "Error updating task. Please try again.")
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Delete Task - Admin Only
@login_required
@user_passes_test(is_admin)
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully! 🗑️")
    return redirect('task_list')

# Register View (Alternative User Signup)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! 🎉 Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "tasks/register.html", {"form": form})




