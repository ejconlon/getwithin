from helpers import *

def index(request):
    return Responder(request, 'layout.html', 'Home').response()

def login_view(request):
  loginform = None
  if request.method == "POST":    
    loginform = LoginForm(request.POST)
    if loginform.login(request):            
      messages.success(request, "Successfully logged in.")
      return HttpResponseRedirect('/')
    else:
      messages.error(request, "Failed to login.")
  else:
    loginform = LoginForm()
  return Responder(request, 'login.html', 'Login').add('form', loginform).response()
  
def logout_view(request):
  logout(request)
  messages.success(request, "Successfully logged out.")
  return HttpResponseRedirect('/')

