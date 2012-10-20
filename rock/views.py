from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect

def base_context_dict(user):
  navlinks = []
  navlinks.append(('Home', '/', False))
  if user is not None and user.is_authenticated():
    #navlinks.append(('Account', '/account', False))
    navlinks.append(('Logout', '/logout', False))
  else:
    #navlinks.append(('Signup', '/signup', False))
    navlinks.append(('Login', '/login', False))
  return {'title': 'GetWithin', 'name': 'GetWithin', 'navlinks': navlinks}

def set_current(d, name):
  d['header'] = name
  l = d['navlinks']
  for i in xrange(len(l)):
    if l[i][0] == name:
      l[i] = (l[i][0], l[i][1], True)
      break

class MyTemplate(object):
  def __init__(self, templatefile, name, user):
    self.t = get_template(templatefile)
    self.name = name
    self.d = base_context_dict(user)
    set_current(self.d, name)
  def html(self):
    return self.t.render(Context(self.d))
  def add(self, name, obj):
    self.d[name] = obj
    return self
  def response(self):
    return HttpResponse(self.html())

def index(request):
    return MyTemplate('layout.html', 'Home', request.user).response()

def login_view(request):
  from helpers import LoginForm
  loginform = None
  if request.method == "POST":    
    loginform = LoginForm(request.POST)
    if loginform.login(request):            
      return HttpResponseRedirect('/')
  else:
    loginform = LoginForm()
  return MyTemplate('login.html', 'Login', request.user).add('form', loginform).response()
  
def logout_view(request):
  from django.contrib.auth import logout
  logout(request)
  return HttpResponseRedirect('/')

