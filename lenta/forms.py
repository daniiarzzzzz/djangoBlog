from django.forms import ModelForm

from lenta.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'image'
        ]