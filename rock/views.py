from helpers import *

def index_view(request):
    return Responder(request, 'landing.html', 'Home').response()

login_view = FormHandler(LoginForm, 'login.html', 'Login', 'Successfully logged in.', 'Failed to log in.', '/').responder()
signup_view = FormHandler(SignupForm, 'signup.html', 'Signup', 'Successfully signed up.', 'Failed to sign up.', '/').responder()
contact_view = FormHandler(PostForm, 'contact.html', 'Contact', 'Thanks for your feedback!', 'Please fill in all fields.', '/').responder()

def logout_view(request):
  logout(request)
  messages.success(request, "Successfully logged out.")
  return HttpResponseRedirect('/')

def search_view(request):
  highlights = TagSet.objects.filter(highlighted=True)
  results = []
  slugs = []
  if request.method == "POST":
    print "POST", request.POST
    for v in request.POST:
      slugs.extend(request.POST.getlist(v))
    print "slugs", slugs
    for activity in Activity.objects.all():
      print "considering activity", activity
      for tag in activity.tag_set.tags.all():
        print "considering tag", tag
        if tag.slug in slugs:
          results.append(activity)
          break
  print "RESULTS", results
  r = Responder(request, 'search.html', 'Search', 'Search')
  r.add('highlights', highlights).add('results', results).add('slugs', slugs)
  return r.response()
