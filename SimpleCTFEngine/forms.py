from django.forms import Form
from django.forms import CharField
from django.forms.widgets import TextInput
from django.forms.widgets import PasswordInput

class LoginForm(Form):
	username = CharField(label = "Username", widget = TextInput())
	password = CharField(label = 'Password', widget = PasswordInput())