from rest_framework import routers
from skills.views import SkillView

route = routers.SimpleRouter()
route.register('skill', SkillView, basename="skill")
urlpatterns = route.urls
