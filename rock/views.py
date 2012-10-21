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

def activity_view(request, slug):
  activity = Activity.objects.get(slug=slug)
  is_into = False
  if request.user is not None:
    is_into = request.user in activity.users.all()
  r = Responder(request, 'activity.html', 'Activity', 'Get withinto...')
  r.add('activity', activity)
  r.add('is_into', is_into)
  r.add('num_into', len(activity.users.all()))
  return r.response()

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
  r.add('num_results', len(results))
  return r.response()

def join_view(request, slug):
  activity = Activity.objects.get(slug=slug)
  assert request.user and request.user not in activity.users.all()
  activity.users.add(request.user) 
  messages.success(request, "Joined "+activity.title)
  return HttpResponseRedirect("/activity/"+slug)

def leave_view(request, slug):
  activity = Activity.objects.get(slug=slug)
  assert request.user and request.user in activity.users.all()
  activity.users.remove(request.user) 
  messages.success(request, "Left "+activity.title)
  return HttpResponseRedirect("/activity/"+slug)

def activities_view(request):
  assert request.user
  results = []
  for activity in Activity.objects.all():
    if request.user in activity.users.all():
      results.append(activity)
  r = Responder(request, 'activities.html', 'Activities', 'Your activities')
  r.add('results', results)
  return r.response()

