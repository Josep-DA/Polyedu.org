from django import forms
from .models import Article, Profile, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.forms import inlineformset_factory
from ckeditor.widgets import CKEditorWidget

# Profile Extras Form
class ProfilePicForm(forms.ModelForm):
	profile_image = forms.ImageField(required=False, label="Profile Picture")
	profile_bio = forms.CharField(required=False, label="Profile Bio", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Profile Bio'}))
	homepage_link = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website Link'}))
	facebook_link =  forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facebook Link'}))
	instagram_link = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Instagram Link'}))
	linkedin_link =  forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Linkedin Link'}))
	
	class Meta:
		model = Profile
		fields = ('profile_image', 'profile_bio', 'homepage_link', 'facebook_link', 'instagram_link', 'linkedin_link', )


class ArticleForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset = Category.objects.all(), required=True,
        widget=forms.widgets.Select(
			attrs={
			"placeholder": "Catégorie de matière",
			"class":"form-control",
   			"id": "category-dropdown",
			}
			), label="Catégorie de matière:"
        )
    
    title = forms.CharField(required=True, 
        widget=forms.widgets.Textarea(
			attrs={
			"placeholder": "Écrivez le titre de l'article.",
			"class":"form-control",
			}
			), label="Titre:"
        )
    desc = forms.CharField(required=True, 
        widget=forms.widgets.Textarea(
			attrs={
			"placeholder": "Écrivez une courte description de l'article.",
			"class":"form-control",
			}
			), label="Description courte:"
        )
    body = forms.CharField(required=True, 
		widget=CKEditorWidget(
			attrs={
			"placeholder": "Écrivez le contenu de votre article ici.",
			}
			), label="Contenu de l'article:"
			
		)
    
    class Meta:
        model = Article
        exclude = ("user", "likes",)
        
    

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class VerbConjugationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.pronouns = ['yo', 'tú', 'él/ella/usted', 'nosotros/nosotras', 'vosotros/vosotras', 'ellos/ellas/ustedes']
        super().__init__(*args, **kwargs)
        for pronoun in self.pronouns:
            self.fields[pronoun] = forms.CharField(label=pronoun, max_length=100)		