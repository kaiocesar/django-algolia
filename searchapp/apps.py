from django.apps import AppConfig
from django.contrib import algoliasearch
from django.contrib.algoliasearch import AlgoliaIndex


class SearchappConfig(AppConfig):
    name = 'searchapp'

    def ready(self):
    	Post = self.get_model('Posts')
    	algoliasearch.register(Post)

class PostsIndex(AlgoliaIndex):
	fields = ('id', 'title', 'content', 'create_at')
	settings = {'attributesToIndex': ['title', 'content']}
	index_name = 'blog_posts'