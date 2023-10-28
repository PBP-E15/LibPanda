from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    CATEGORY_CHOICES = (
        ('', 'Choose Category'),  
        ('Fiction', 'Fiction'),
        ('History', 'History'),
        ('Cooking', 'Cooking'),
        ('Graphic Novels', 'Graphic Novels'),
        ('Philosophy', 'Philosophy'),
    )

    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'id_title', 'placeholder': 'Enter the title of the book', 'class': 'form-control'}),
        required=True,
    )
    author = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'id_author', 'placeholder': 'Enter the author of the book', 'class': 'form-control'}),
        required=True,
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'id': 'id_category', 'placeholder': 'Choose Category', 'class': 'form-control'}),
        required=True, 
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'id_year', 'placeholder': 'Enter the year the book was published', 'class': 'form-control'}),
        required=True, 
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'year']