from django import forms 
from .models import Product, Category, STAR_RATING, Review
from .widgets import CustomClearableFileInput
from .models import Review, STAR_RATING


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs )
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class RateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    
    rated = forms.ChoiceField(choices=STAR_RATING, widget=forms.Select(), required=True)

    class Meta:
        model = Review
        exclude = (
            'user',
            'date',
            'product',
            'likes',
            )

        fields = ['review', 'rated', ]

       
    
