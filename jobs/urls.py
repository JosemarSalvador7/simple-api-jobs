from rest_framework import routers
from jobs.views import JobView

route = routers.SimpleRouter()
route.register('job', JobView, basename="job")
urlpatterns = route.urls
