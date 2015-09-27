from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core.context_processors import csrf

from models import KeyProfile
from models import KeySolves
from forms import LoginForm

def login(request):
	context = {}
	context.update(csrf(request))
	if request.method == "POST":
		user = authenticate(username=request.REQUEST.get('username'), password=request.REQUEST.get('password'))
		# handle error cases, inactive users, ...
		login(request, user)
		print "we logged the person in I think"
	elif request.method == "GET":
		context['form'] = LoginForm()
		return render(request, 'login.html', context)

def home(request):
	keyProfiles = KeyProfile.objects.all()
	keySolves = KeySolves.objects.filter(user = user)
	context = {'keyProfiles': keyProfiles, 'keySolves': keySolves}
	return render(request, 'home.html', context)

def submitKey(request, keyId):
	keySolved = KeySolves.objects.get(user = request.user, id = keyId)
	if keySolved:
		# Person has already solved this key
		return render(request, 'home.html')
	# Is the key correct?
	keyProfile = KeyProfile.objects.get(id = keyId)
	if request.POST['key'] == keyProfile.key:
		# Key is correct
		context = {"message": "Congradulations, you got the key!"}
		keySolved(keyId = keyProfile, userId = request.user).save()
	else:
		# Key is incorrect
		context = {"message": "I'm sorry, that key is incorrect."}
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'message': latest_question_list}
	return render(request, 'submitKey.html', context)

def overview(request):
	context = {}
	return render(request, 'overview.html', context)