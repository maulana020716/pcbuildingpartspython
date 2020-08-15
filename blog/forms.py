from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text','thumb_pic')
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["author"].label = "Penulis"
        self.fields["title"].label = "Judul"
        self.fields["text"].label = "Isi Konten"
        self.fields["thumb_pic"].label = "Gambar Thumbnail"


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["author"].label = "Penulis"
        self.fields["text"].label = "Komentar"
