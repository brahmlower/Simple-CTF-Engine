from django.db.models import Model
from django.db.models import AutoField
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import DateTimeField
from django.utils import timezone
from django.contrib.auth.models import User

class KeyProfile(Model):
	id = AutoField(primary_key = True)
	key = CharField(max_length = 128)
	description = CharField(max_length = 400)

class KeySolves(Model):
	id = AutoField(primary_key = True)
	keyId = ForeignKey(KeyProfile)
	userId = ForeignKey(User)
	datetime = DateTimeField(default = timezone.now())
