SECRET_KEY = 'SOME-LONG-SECRET-KEY-GOES-HERE'

ldap_dc_suffix = "dc=example,dc=local"

AUTH_LDAP_SERVER_URI = "ldap://ad.example.local"
AUTH_LDAP_BIND_DN = "cn=django-agent,ou=users," + ldap_dc_suffix
AUTH_LDAP_BIND_PASSWORD = "django-agent-password"

LDAP_USER_SEARCH_BASE = ldap_dc_suffix
LDAP_GROUP_SEARCH_BASE = ldap_dc_suffix