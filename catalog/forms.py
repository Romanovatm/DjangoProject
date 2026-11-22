from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price',]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену продукта'})
        self.fields['category'].label = 'Категория'
        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError('Имя содержит запрещенные слова')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description') or ''
        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError('Описание содержит запрещенные слова')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError('Цена продукта не может быть отрицательной или равняться нулю')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if isinstance(image, UploadedFile):
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Размер изображения не должен превышать 5 МБ')
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise ValidationError('Допустимы только изображения в формате JPEG или PNG')
        return image
