from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from flace.models import Post
from flace.serializers import PostSerializer

def homepage(self):
	template = loader.get_template('bio.html')
	return HttpResponse(template.render())

def trips(self):
	# TODO add pagination
	template = loader.get_template('trips.html')
	return HttpResponse(template.render())

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
		# try:
		# 	post = Post.objects.get(pk = pk)
		# except Post.DoesNotExist:
		# 	return HttpResponse(status = 404)

		# 	if request.method == 'GET':
		# 		serializer = SnippetSerializer(snippet)
		# 		return JSONResponse(serializer.data)

		# 	elif request.method == 'PUT':
		# 		data = JSONParser().parse(request)
		# 		serializer = SnippetSerializer(snippet, data=data)
		# 		if serializer.is_valid():
		# 			serializer.save()
		# 			return JSONResponse(serializer.data)
		# 			return JSONResponse(serializer.errors, status=400)

		# 		elif request.method == 'DELETE':
		# 			snippet.delete()
		# 			return HttpResponse(status=204)

		# 	return post
		return null
