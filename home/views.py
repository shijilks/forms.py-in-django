from django.shortcuts import render
from . import forms
# Create your views here.

def your_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("validation Success !!!")
            print('Name:'+ form.cleaned_data['name'])
            print('Email:'+ form.cleaned_data['Email'])
            print('Description:'+ form.cleaned_data['description'])
    return render(request, 'index.html', {'form': form})