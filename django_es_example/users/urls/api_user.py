from rest_framework.routers import DefaultRouter

from django_es_example.users.views import UserElasticViewSet

router = DefaultRouter()
router.register(r'api/user', UserElasticViewSet, base_name='api_user')
api_user_urlpatterns = router.urls
