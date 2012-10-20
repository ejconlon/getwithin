from helpers import *

def index_view(request):
    return Responder(request, 'layout.html', 'Home').response()

def login_view(request):
  form = None
  if request.method == "POST":    
    form = LoginForm(request.POST)
    if form.fill(request):            
      messages.success(request, "Successfully logged in.")
      return HttpResponseRedirect('/')
    else:
      messages.error(request, "Failed to log in.")
  else:
    form = LoginForm()
  return Responder(request, 'login.html', 'Login').add('form', form).response()

def signup_view(request):
  form = None
  if request.method == "POST":    
    form = SignupForm(request.POST)
    if form.fill(request):            
      messages.success(request, "Successfully signed up.")
      return HttpResponseRedirect('/')
    else:
      messages.error(request, "Failed to sign up.")
  else:
    form = LoginForm()
  return Responder(request, 'signup.html', 'Signup').add('form', form).response()
  
def logout_view(request):
  logout(request)
  messages.success(request, "Successfully logged out.")
  return HttpResponseRedirect('/')

