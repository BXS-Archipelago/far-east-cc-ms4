from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    User to input data here for review
    """
    class Meta:
        model = Review
        exclude = (
            'user',
            'date_added',
            'product',
            )

        fields = ['title', 'description', 'rating']

        labels = {
            'rating': 'Rating',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Description',
        }
