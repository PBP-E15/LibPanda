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

    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'id': 'id_category'})
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'year']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'id_title', 'placeholder': 'Masukkan judul buku'}),
            'author': forms.TextInput(attrs={'id': 'id_author', 'placeholder': 'Masukkan nama penulis'}),
            'year': forms.NumberInput(attrs={'id': 'id_year', 'placeholder': 'Masukkan tahun terbit'}),
        }
        labels = {
            'title': 'Judul Buku',
            'author': 'Penulis',
            'category': 'Kategori',
            'year': 'Tahun Terbit',
        }