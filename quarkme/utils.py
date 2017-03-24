from django.contrib.auth.models import User

def get_login_user(cookie):
	username = cookie.get('username', None)
	if not username:
		return None
	users = User.objects.filter(user__username=username)
	if len(users) > 0:
		return users[0]
	return None