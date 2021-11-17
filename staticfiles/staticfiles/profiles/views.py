from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView

from .models import profile


class FollowView(View):

    def post(self, request, *args, **kwargs):
        my_profile = profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
            obj.follower.remove(my_profile.user)
        else:
            my_profile.following.add(obj.user)
            obj.follower.add(my_profile.user)

        return redirect(request.META.get('HTTP_REFERER'))


class ProfilesDetailView(DetailView):
    model = profile
    template_name = 'post_detail.html'
