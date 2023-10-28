from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    CATEGORY_CHOICES = (
        ('', 'Pilih kategori'),  
        ('Fiksi', 'Fiksi'),
        ('Sejarah', 'Sejarah'),
        ('Makanan & Minuman', 'Makanan & Minuman'),
        ('Komik & Novel Grafis', 'Komik & Novel Grafis'),
        ('Filosofi', 'Filosofi'),
    )

    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'id_title', 'placeholder': 'Masukkan judul buku', 'class': 'form-control'}),
        required=True,
        label='Judul Buku'  
    )
    author = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'id_author', 'placeholder': 'Masukkan nama penulis', 'class': 'form-control'}),
        required=True,
        label='Penulis' 
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'id': 'id_category', 'placeholder': 'Pilih kategori', 'class': 'form-control'}),
        required=True,
        label='Kategori'  
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'id_year', 'placeholder': 'Masukkan tahun terbit', 'class': 'form-control'}),
        required=True,
        label='Tahun Terbit'  
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'year']