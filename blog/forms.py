from django import forms

from .models import Post, Chemie, German, Russian

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)

class ChemieForm(forms.ModelForm):

	class Meta:
		model = Chemie
		fields = ('title', 'text',)

class GermanForm(forms.ModelForm):

	class Meta:
		model = German
		fields = ('title', 'text',)

class RussianForm(forms.ModelForm):

	class Meta:
		model = Russian
		fields = ('title', 'text',)
