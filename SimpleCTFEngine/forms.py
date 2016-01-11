from django.forms import Form
from django.forms import ModelForm
from django.forms import CharField
from django.forms.widgets import TextInput
from django.forms.widgets import PasswordInput
from models import KeyProfile

bs_attrs = {'class':'form-control'}

class LoginForm(Form):
	username = CharField(label = "Username", widget = TextInput())
	password = CharField(label = 'Password', widget = PasswordInput())

class KeySubmitForm(Form):
	key = CharField(label = "Key", widget = TextInput())

class KeyCreateForm(ModelForm):
	class Meta:
		model = KeyProfile
		fields = ['name', 'key', 'description']
	name = CharField(label = 'Name', widget = TextInput(attrs = bs_attrs))
	key = CharField(label = 'Key', widget = TextInput(attrs = bs_attrs))
	description = CharField(label = 'Description', widget = TextInput(attrs = bs_attrs), required = False)

class SettingsForm(Form):
	ldap_server_uri = CharField(label = "Server URI", widget = TextInput())
	ldap_bind_dn = CharField(label = "Username", widget = TextInput())
	ldap_bind_dn_password = CharField(label = "Password", widget = PasswordInput())
	ldap_user_search = CharField(label = "User Search", widget = TextInput())
	ldap_group_search = CharField(label = "Group Search", widget = TextInput())
