from django.shortcuts import render
from searchapp.models import Posts


def index(request):
	posts = Posts.objects.all()[:5]
	context = {
		'posts': posts
	}
	return render(request, 'index.html', context)

def show(request, id):
	post = Posts.objects.get(pk=id)
	return render(request, 'show.html', {'post':post})