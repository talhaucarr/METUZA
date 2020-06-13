from django import forms

from .models import ClassHomework, ClassContent, NewClass, Homework, ClassPost


class NewClassForm(forms.ModelForm):
    class Meta:
        model = NewClass
        fields = ["class_name", "class_code"]


class NewContentForm(forms.ModelForm):
    class Meta:
        model = ClassContent
        fields = ["student_name", "classroom"]


class NewHomeworkForm(forms.ModelForm):
    class Meta:
        model = ClassHomework
        fields = ["title", "content", "end_date", "end_clock"]


class _NewHomeworkDeliveryForm(forms.ModelForm):
    class Meta:
        model = ClassHomework
        fields = ['files']


class SecondHomework(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ["title", "content", "end_date", "end_clock", "end_clock", "is_end", "homework_code", "submit_count"]


class ClassPostForm(forms.ModelForm):
    class Meta:
        model = ClassPost
        fields = ["title", "content", "files"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = ClassHomework
        fields = ["student_name", "title", "files", "note", ]
