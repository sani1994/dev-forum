from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View

from post_app.forms import PostForm


class PostCreationView(View):

    template = 'posts/create-post.html'

    def get(self, request):
        post_form = PostForm()
        context = {'post_form': post_form}
        return render(request, self.template, context=context)
