from django import forms
from .models import Post, Profile, WorkExperience


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "name", "surname", "about", "instagram", "twitter", "facebook", "github", "linkedin",
                  "pinterest", "high_school", "started_date_high_school",
                  "end_date_high_school", "university", "started_date_university", "end_date_university",
                  "master_degree", "started_date_master_degree", "end_date_master_degree", "phd", "started_date_phd",
                  "end_date_phd"]


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ["company", "position", "started_date", "end_date"]


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı:")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı:")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parolayı Doğrula", widget=forms.PasswordInput)
    email = forms.CharField(max_length=50, label="E-mail")

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        if (email.find("@") != -1 and email.endswith(".com")) == False:
            raise forms.ValidationError("Geçersiz e-mail")

        values = {
            "username": username,
            "password": password,
            "email": email,
        }
        return values