from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from django_es_example.users.serializer.user import UserElasticInfoSerializer

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserListView(LoginRequiredMixin, ListView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_list_view = UserListView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


# Your stuff: custom views here

class UserElasticViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserElasticInfoSerializer
