
from django.http import HttpResponse
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from flace.models import Post, User
from flace.serializers import PostSerializer, UserSerializer

def index(self):
	# print("THIS IS THE REQUEsT" + request)
	template = loader.get_template('header.html')
	context = Context({})
	return HttpResponse()


class JSONResponse(HttpResponse):

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['consingletent_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

	@csrf_exempt
	def get_posts(request):
		if request.method == 'GET':
			posts = Post.objects.all()
			serializer = PostSerializer(posts, many=True)
			return JSONResponse(serializer.data)

		elif request.method == 'POST':
			data = JSONParser().parse(request)
			serializer = PostSerializer(data = data)

			if serializer.is_valid():
				serializer.save()
				return JSONResponse(serializer.data, status=201)
				return JSONResponse(serializer.errors, status = 400)

	@csrf_exempt
	def get_post(request, pk):
		try:
			post = Posts.objects.get(pk = pk)
		except Post.DoesNotExist:
			return HttpResponse(status = 404)

			if request.method == 'GET':
				serializer = SnippetSerializer(snippet)
				return JSONResponse(serializer.data)

			elif request.method == 'PUT':
				data = JSONParser().parse(request)
				serializer = SnippetSerializer(snippet, data=data)
				if serializer.is_valid():
					serializer.save()
					return JSONResponse(serializer.data)
					return JSONResponse(serializer.errors, status=400)

				elif request.method == 'DELETE':
					snippet.delete()
					return HttpResponse(status=204)



