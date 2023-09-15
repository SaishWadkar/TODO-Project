from django import forms
from note_app.models import Note

# class NewItemForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Desc', 'style': 'width: 300px;', 'class': 'form-control'}))


class NewItemForm(forms.ModelForm):

    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Desc', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = Note
        fields = ('title','description')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'placeholder': 'Desc', 'style': 'width: 300px;', 'class': 'form-control'})
        }
