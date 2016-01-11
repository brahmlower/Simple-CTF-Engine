# Simple-CTF-Engine
This is a simple CTF engine for the UAF CSC lectures

<img src="http://i.imgur.com/DlNOop3.png" alt="Main page/score board" width="32%">
<img src="http://i.imgur.com/xoxiAnV.png" alt="Key creation page" width="32%">
<img src="http://i.imgur.com/S2TwiMp.png" alt="Key submission page" width="32%">

## Ubuntu Install
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential libldap2-dev libsasl2-dev python-dev python-pip
git clone https://github.com/bplower/Simple-CTF-Engine.git
cd Simple-CTF-Engine
sudo pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver
```

### secretConfigs.py
Authentication is meant to be done via LDAP/AD. Before running the server, make sure you have created the secretConfigs.py file within the Simple-CTF-Engine directory. There is an example file called secretConfigs-example.py in the same directory. The values that should be in the file are as follows:

**SECRET_KEY**<br>
This is the key that django uses. It's not good to run a publicly available key on a production system, so replace this string with some long line of gibberish.
<br>```SECRET_KEY = 'SOME-LONG-SECRET-KEY-GOES-HERE'```

**AUTH_LDAP_SERVER_URI**<br>
This is the URI for the location of the domain controller. If the FQDN for your domain controller was ad.example.com, then your URI would be as follows.
<br>```AUTH_LDAP_SERVER_URI = "ldap://ad.example.com"```

**AUTH_LDAP_BIND_DN**<br>
This is the distinguished name for the user to authenticate as with the domain controller. This should point directly to your user with the 'cn'. The following would point to the domain administrator in a default environment. Don't authenticate with your domain controller using your domain administrator- that's a very bad idea...
<br>```AUTH_LDAP_BIND_DN = "cn=administrator,ou=Users,dc=example,dc=com"```

**AUTH_LDAP_BIND_PASSWORD**<br>
This is the password for the user account that was specified in the previous section.
<br>```AUTH_LDAP_BIND_PASSWORD = "django-agent-password"```
