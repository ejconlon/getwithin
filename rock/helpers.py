from django.utils.translation import ugettext_lazy as _, ugettext
from django import forms
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from models import Post
import datetime

def base_context_dict(user):
  navlinks = []
  navlinks.append(('Home', '/', False))
  navlinks.append(('Contact', '/contact', False))
  if user is not None and user.is_authenticated():
    #navlinks.append(('Account', '/account', False))
    navlinks.append(('Logout '+user.username, '/logout', False))
  else:
    navlinks.append(('Signup', '/signup', False))
    navlinks.append(('Login', '/login', False))
  return {'title': 'GetWithin', 'name': 'GetWithin', 'navlinks': navlinks}

def set_current(d, name):
  d['header'] = name
  l = d['navlinks']
  for i in xrange(len(l)):
    if l[i][0].startswith(name):
      l[i] = (l[i][0], l[i][1], True)
      break

class FormHandler(object):
  def __init__(self, klass, templatefile, name, success_msg, failure_msg, redir_url):
    self.klass = klass
    self.templatefile = templatefile
    self.name = name
    self.success_msg = success_msg
    self.failure_msg = failure_msg
    self.redir_url = redir_url
  def responder(self):
    def func(request):
      form = None
      if request.method == "POST":    
        form = self.klass(request.POST)
        if form.fill(request):            
          messages.success(request, self.success_msg)
          return HttpResponseRedirect(self.redir_url)
        else:
          messages.error(request, self.failure_msg)
      else:
        form = self.klass()
      return Responder(request, self.templatefile, self.name).add('form', form).response()
    return func

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
  email = forms.CharField(label=_('Email'))
  password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)        
  user = None   # allow access to user object     

  def clean(self):
    # only do further checks if the rest was valid
    if self._errors: return

    user = authenticate(username=self.data['email'], password = self.data['password'])
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

  def fill(self, request):
    if self.is_valid():
      login(request, self.user)
      return True
    return False

class SignupForm(forms.Form):
  email = forms.CharField(label=_('Email'))
  password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)        

  def is_present(self, name):
    return len(self.data[name]) > 0

  def clean(self):
    if self._errors: return
    if not self.is_present('email') or not self.is_present('password'):
      raise forms.ValidationError(ugettext('Please fill in all fields.'))
    elif len(User.objects.filter(username=self.data['email'])) > 0:
      raise forms.ValidationError(ugettext('That email has already been registered.'))
    else:
      return self.cleaned_data

  def fill(self, request):
    if self.is_valid():
      User.objects.create_user(self.data['email'], self.data['email'], self.data['password'])
      user = authenticate(username=self.data['email'], password = self.data['password'])
      login(request, user)
      return True
    return False

class PostForm(forms.Form):
  title = forms.CharField(label=_('Subject'))
  body = forms.CharField(label=_('Message'))

  def is_present(self, name):
    return len(self.data[name]) > 0

  def clean(self):
    if self._errors: return
    if not self.is_present('title') or not self.is_present('body'):
      raise forms.ValidationError(ugettext('Please fill in all fields.'))
    else:
      return self.cleaned_data

  def fill(self, request):
    if self.is_valid():
      now = datetime.datetime.now()
      Post.objects.create(title=self.data['title'], body=self.data['body'], pub_date=now)
      return True
    return False


