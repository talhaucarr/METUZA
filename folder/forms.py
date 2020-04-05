from django import forms

from .models import Book, BookStory, BookPersonal, BookMath


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')


class BookStoryForm(forms.ModelForm):
    class Meta:
        model = BookStory
        fields = ('title', 'author', 'pdf', 'cover')


class BookPersonalForm(forms.ModelForm):
    class Meta:
        model = BookPersonal
        fields = ('title', 'author', 'pdf', 'cover')


class BookMathForm(forms.ModelForm):
    class Meta:
        model = BookMath
        fields = ('title', 'author', 'pdf', 'cover')
