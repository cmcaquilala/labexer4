from django.forms import ModelForm
from .models import *

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

        # fields = {'name', 'stars', 'role'}
        # labels = {
        #     'name' : "Character name:",
        #     'stars' : '4 or 5 star',
        #     'role' : 'Role (comma if multiple)'
        # }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        # labels = {
        #     'title' : "titulo",
        # }