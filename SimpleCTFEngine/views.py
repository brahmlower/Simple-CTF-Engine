from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.context_processors import csrf

from models import KeyProfile
from models import KeySolves
from forms import LoginForm

def login(request):
	context = {}
	context.update(csrf(request))
	context['form'] = LoginForm()
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user is not None:
			if user is not None:
				auth_login(request, user)
				print "we logged the person in I think"
				return redirect('/home')
			else:
				context['message'] = 'Account locked or disabled.'
		else:
			context['message'] = 'Incorrect username or password.'
	return render(request, 'login.html', context)

def logout(request):
	auth_logout(request)
	return redirect('/overview')

def home(request):
	if not request.user.is_authenticated():
		return redirect('/login')
	context = {}
	context['user'] = request.user 
	context['keyProfiles'] = KeyProfile.objects.all()
	context['keySolves'] = KeySolves.objects.filter(userId = request.user)
	return render(request, 'home.html', context)

def submitKey(request, keyId):
	keySolved = KeySolves.objects.get(userId = request.user, keyId = keyId)
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