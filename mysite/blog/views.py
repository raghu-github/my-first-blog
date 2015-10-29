from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from blog.models import Post


# Create your views here.
# def getPost(request):
# 	posts = Post.objects.all()[0]
# 	html = "<html><body> Latest post is: %s </body></html>" %posts
# 	return HttpResponse(html)
def displaypost(request):
	posts = Post.objects.all()
	t = loader.get_template('blog/displaypost.html') 
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))

