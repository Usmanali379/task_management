from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from .models import Project

# Common Tailwind CSS classes for input fields
TAILWIND_INPUT_CLASSES = "w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
TAILWIND_SELECT_CLASSES = f"{TAILWIND_INPUT_CLASSES} bg-white"
TAILWIND_TEXTAREA_CLASSES = f"{TAILWIND_INPUT_CLASSES} h-32 resize-none"

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply styling to each field
        self.fields['username'].widget.attrs.update({'class': TAILWIND_INPUT_CLASSES})
        self.fields['email'].widget.attrs.update({'class': TAILWIND_INPUT_CLASSES})
        self.fields['password1'].widget.attrs.update({'class': TAILWIND_INPUT_CLASSES})
        self.fields['password2'].widget.attrs.update({'class': TAILWIND_INPUT_CLASSES})
        
        # You can also update placeholders if desired
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your email address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'type':'date'
            }
        )
    )   
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'status', 'project']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply styling to text/date fields
        self.fields['title'].widget.attrs.update({'class': TAILWIND_INPUT_CLASSES})
        self.fields['description'].widget.attrs.update({'class': TAILWIND_TEXTAREA_CLASSES})
        self.fields['due_date'].widget.attrs.update({'class': TAILWIND_INPUT_CLASSES})
        
        # Apply styling to select/dropdown fields
        self.fields['priority'].widget.attrs.update({'class': TAILWIND_SELECT_CLASSES})
        self.fields['status'].widget.attrs.update({'class': TAILWIND_SELECT_CLASSES})
        self.fields['project'].widget.attrs.update({'class': TAILWIND_SELECT_CLASSES})
        
        self.fields['project'].queryset = Project.objects.all().order_by('name')
        # Optional: Add placeholders
        self.fields['title'].widget.attrs.update({'placeholder': 'Task title'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Task description'})