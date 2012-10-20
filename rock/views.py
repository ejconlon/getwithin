from helpers import *

def index_view(request):
    return Responder(request, 'layout.html', 'Home').response()

login_view = FormHandler(LoginForm, 'login.html', 'Login', 'Successfully logged in.', 'Failed to log in.', '/').responder()
signup_view = FormHandler(SignupForm, 'signup.html', 'Signup', 'Successfully signed up.', 'Failed to sign up.', '/').responder()
contact_view = FormHandler(PostForm, 'contact.html', 'Contact', 'Thanks for your feedback!', 'Please fill in all fields.', '/').responder()

def logout_view(request):
  logout(request)
  messages.success(request, "Successfully logged out.")
  return HttpResponseRedirect('/')

