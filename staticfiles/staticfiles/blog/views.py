from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

from blog_project.tasks import send_mail_func
from profiles.models import profile
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            my_profile = profile.objects.get(user=self.request.user.id)
            user_count = my_profile.following.all().count()
            user_follower = my_profile.follower.all().count()
            context["user_count"] = user_count
            context["user_follower"] = user_follower
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Post.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get("object").pk
        view_profile_post = Post.objects.get(pk=pk)
        author_id = view_profile_post.author.id
        author = profile.objects.get(pk=author_id)
        follower_count = author.follower.all().count()
        following_count = author.following.all().count()
        try:
            my_profile = profile.objects.get(user=self.request.user.id)
        except profile.DoesNotExist:
            pass

        if view_profile_post.author in my_profile.following.all():
            check_follow = True
        else:
            check_follow = False
        context["follow"] = check_follow
        context["follower_count"] = follower_count
        context["following_count"] = following_count
        return context


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        send_mail_func.delay(obj.author.id)
        return HttpResponseRedirect(self.success_url)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


# def detail_page(request, pk):
# detail = Post.objects.get(id=pk)
# serialized_data = CrudSerializer(detail)
# json_data = JSONRenderer().render(serialized_data.data)
# return HttpResponse(json_data, content_type='application/json')


# def detail_all(request):
# detail = Post.objects.all()
# serialized_data = CrudSerializer(detail, many=True)
# json_data = JSONRenderer().render(serialized_data.data)
# return HttpResponse(json_data, content_type='application/json')

# @csrf_exempt
# def detail_create(request):
# if request.method == "POST":
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     python_data = JSONParser().parse(stream)
#     #pythondata.author = 'mehrab'
#     serializedDATA = CrudSerializer(data=python_data)
#     if serializedDATA.is_valid():
#         serializedDATA.save()
#         res = {'msg': 'Data Created'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
#
#     json_data = JSONRenderer().render(serializedDATA.errors)
#     return HttpResponse(json_data, content_type='application/json')
#
# if request.method == "PUT":
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     python_data = JSONParser().parse(stream)
#     id = python_data.get('id')
#     pt_id = Post.objects.get(id=id)
#     serializedDATA = CrudSerializer(pt_id, data=python_data, partial=True)
#     if serializedDATA.is_valid():
#         serializedDATA.save()
#         res = {'msg': 'Data Updated'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
#
#     json_data = JSONRenderer().render(serializedDATA.errors)
#     return HttpResponse(json_data, content_type='application/json')
#
# if request.method == "DELETE":
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     python_data = JSONParser().parse(stream)
#     id = python_data.get('id')
#     pt_id = Post.objects.get(id=id)
#     pt_id.delete()
#     res = {'msg': 'Data Delete'}
#     json_data = JSONRenderer().render(res)
#     return HttpResponse(json_data, content_type='application/json')

def follower_list(request):
    return render(request, 'follower_list.html')


def following_list(request):
    return render(request, 'following_list.html')
