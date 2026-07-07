from django.urls import path

from skills import views

app_name = "skills"

urlpatterns = [
    path("", views.SkillListView.as_view(), name="list"),
    path("<int:pk>/", views.SkillDetailView.as_view(), name="details"),
]
