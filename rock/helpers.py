from django.utils.translation import ugettext_lazy as _, ugettext
from django import forms
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

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

class Responder(object):
  def __init__(self, request, templatefile, name):
    self.request = request
    self.templatefile = templatefile
    self.name = name
    self.t = get_template(templatefile)
    self.d = base_context_dict(request.user)
    set_current(self.d, name)
  def html(self):
    self.add('messages', messages.get_messages(self.request))
    return self.t.render(Context(self.d))
  def add(self, name, obj):
    self.d[name] = obj
    return self
  def response(self):
    return HttpResponse(self.html())

class LoginForm(forms.Form):
  username = forms.CharField(label=_('Username'))
  password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)        
  user = None   # allow access to user object     

  def clean(self):
    # only do further checks if the rest was valid
    if self._errors: return

    user = authenticate(username=self.data['username'],
    password = self.data['password'])
    if user is not None:
      if user.is_active:
        self.user = user                    
      else:
        raise forms.ValidationError(ugettext(
          'This account is currently inactive. Please contact '
          'the administrator if you believe this to be in error.'))
    else:
      raise forms.ValidationError(ugettext(
        'The username and password you specified are not valid.'))
    return self.cleaned_data

  def login(self, request):
    if self.is_valid():
      login(request, self.user)
      return True
    return False
