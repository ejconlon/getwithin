from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def base_context_dict():
  navlinks = []
  navlinks.append(('Home', '/', True))
  return {'title': 'GetWithin', 'name': 'GetWithin', 'navlinks': navlinks}

def index(request):
    t = get_template('layout.html')
    d = base_context_dict()
    d['header'] = 'Home'
    html = t.render(Context(d))
    return HttpResponse(html)
