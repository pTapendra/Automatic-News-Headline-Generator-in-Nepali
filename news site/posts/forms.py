# FOR HELP: https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from markdownx.fields import MarkdownxFormField

from .models import *

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='शीर्षक:' )

    body = MarkdownxFormField(label='समाचार:' )

    category = forms.CharField(label='वर्ग: ', widget=forms.Select(
        choices=[('politics', 'राजनीति'),
                 ('national', 'राष्ट्रिय'),
                 ('international', 'अन्तर्राष्ट्रिय'),
                 ('finance', 'आर्थिक'),
                 ('sports', 'खेलकुद'),
                 ('others', 'अन्य'),
                 ]))

    image = forms.ImageField(required=False,
        label = "फोटो: ")

    private_post = forms.BooleanField(required=False, label='प्राइभेट पोष्ट')
    use_preeti = forms.BooleanField(required=False, label='मा प्रीति फन्ट प्रयोग गर्छु')

    class Meta:
        model = Post
        fields = [ 'title','body','category','private_post','image','use_preeti']

    # TODO: make this work
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='my-5'),
        )


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'कमेन्ट टाईप गर्नुहोस ...',
            'rows':2
            }))

    image = forms.ImageField(required=False,
        label = "यहाँ एउटा फोटो अपलोड गर्न सक्नुहुन्छ: ")

    class Meta:
        model = Answer
        fields = ['answer', 'image']
