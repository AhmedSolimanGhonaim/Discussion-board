from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3  border-0 shadow-sm  bg-light' ,
            'id': 'id_message',
            'rows': 5,
            'required': 'required',
             'name': 'message',
             'placeholder': 'What is your question?',
             'maxlength': 4000 
        }),
        max_length=4000,
        help_text='The max length of the text is 4000 characters'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_subject',
                'required': 'required'
            }),
        }
