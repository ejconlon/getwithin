from django.utils.translation import ugettext_lazy as _, ugettext
from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(label=_('Username'))
  password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)        
  user = None   # allow access to user object     

  def clean(self):
    # only do further checks if the rest was valid
    if self._errors: return

    from django.contrib.auth import login, authenticate
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
    from django.contrib.auth import login
    if self.is_valid():
      login(request, self.user)
      return True
    return False
