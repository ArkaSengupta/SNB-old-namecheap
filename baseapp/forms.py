from django import forms
from .models import Query, Career

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'
        exclude = ['id','date_created']

    # def clean_content(self):
    #     content = self.cleaned_data.get("content")
    #     if len(content) > MAX_TWEET_LENGTH:
    #         raise forms.ValidationError("This tweet is too long")
    #     return content
class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = '__all__'
        exclude = ['id','date_created']
        widgets = {
            'DOB': forms.SelectDateWidget(),
        }
