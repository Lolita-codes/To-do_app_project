from django import forms


class ToDoForm(forms.Form):
    item = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Enter to-do e.g Cook and Clean',
                                      'aria-label': 'Todo',
                                      'aria-describedby': 'add-btn'}
                           ))
