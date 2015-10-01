from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.context_processors import csrf

from models import KeyProfile
from models import KeySolves
from forms import LoginForm
from forms import KeySubmitForm

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
	context['form'] = KeySubmitForm()
	keyProfileObjects = KeyProfile.objects.all()
	context['key'] = []
	for i in keyProfileObjects:
		tmpDict = {}
		tmpDict['id'] = i.id
		tmpDict['name'] = i.name
		tmpDict['description'] = i.description
		try:
			KeySolves.objects.get(userId = request.user, keyId = i.id)
			tmpDict['solved'] = True
		except KeySolves.DoesNotExist:
			tmpDict['solved'] = False
		context['key'].append(tmpDict)
	return render(request, 'home.html', context)

def submitKey(request, keyId):
	if not request.user.is_authenticated():
		return redirect('/overview')
	if request.method != 'POST':
		return redirect('/home')

	try:
		keySolved = KeySolves.objects.get(userId = request.user, keyId = keyId)
		# Person has already solved this key
		return redirect('/home')
	except KeySolves.DoesNotExist:
		pass
		
	# Is the key correct?
	keyProfile = KeyProfile.objects.get(id = keyId)
	if request.POST['key'] == keyProfile.key:
		# Key is correct
		KeySolves(keyId = keyProfile, userId = request.user).save()
	return redirect('/home')

def overview(request):
	context = {}
	context['keySolves'] = KeySolves.objects.all()
	return render(request, 'overview.html', context)