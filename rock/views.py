from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def base_context_dict():
  navlinks = []
  navlinks.append(('Home', '/', False))
  return {'title': 'GetWithin', 'name': 'GetWithin', 'navlinks': navlinks}

def set_current(d, name):
  d['header'] = name
  l = d['navlinks']
  for i in xrange(len(l)):
    if l[i][0] == name:
      l[i] = (l[i][0], l[i][1], True)
      break

def index(request):
    t = get_template('layout.html')
    d = base_context_dict()
    set_current(d, 'Home')
    html = t.render(Context(d))
    return HttpResponse(html)
