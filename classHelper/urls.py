from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from classHelper import views

router = DefaultRouter()
router.register(r'problemset', views.ProblemSetViewSet)
router.register(r'classuser', views.ClassUserViewSet)
router.register(r'problem', views.ProblemViewSet)
router.register(r'solution', views.SolutionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
