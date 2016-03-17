from django.http import HttpResponse
from django.template import loader, Context

def homepage(self):
	template = loader.get_template('header.html')
	return HttpResponse(template.render())
