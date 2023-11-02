from django.forms import ModelForm 
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms

class MyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']
        self.fields['user_picture'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['user_picture']

class LoginForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = User
        fields = ['username', "password"]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='',
                             widget=forms.TextInput(
                                {'class': 'form-control', 
                                'placeholder': 'Email Adress'})
                            )

    first_name = forms.CharField(label='',
                            max_length=100,
                            widget=forms.TextInput(
                                {'class': 'form-control', 
                                'placeholder': 'Ism'})
                        )
    last_name = forms.CharField(label='',
                        max_length=100,
                        widget=forms.TextInput(
                            {'class': 'form-control', 
                            'placeholder': 'Familiya'})
                    )

    class Meta:
        model = User
        fields = ('username', 'first_name' ,'last_name', 'email', 'password1', 'password2') 

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>To\'dirish muhim. 50 yoki undan kam belgidan foydalaning. Faqat harflar, raqamlar va @/./+/-/_ belgilardan foydalanish mumkin.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Parol'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Parolinggiz boshqa shaxsiy ma\'lumotlaringiz bilan o\'xshash bo\'lmasligi kerak.</li><li>Parolingiz kamida 8 ta belgidan iborat bo\'lishi lozim.</li><li>Parolinggiz juda ham oddiy bo\'lmasligi lozim.</li><li>Parolingiz faqat raqamlardan iborat bo\'lmasligi lozim.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Parolni tasdiqlash'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Tasdiqlash uchun yuqorida kiritilgan parol bilan bir xil parolni kiriting.</small></span>'



