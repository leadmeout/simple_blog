from django.shortcuts import render

# Create your views here.
def blog_post_list(request):
	return render(request, 'blog_posts/blog_post_list.html', {})