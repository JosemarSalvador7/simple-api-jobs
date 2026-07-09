from rest_framework import routers
from jobs.views import JobView

route = routers.SimpleRouter()
route.register(r"", JobView, basename="jobs")
urlpatterns = route.urls
