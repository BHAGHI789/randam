from django.urls import path
from app.views import create_profile, update_profile,List_Profile
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", List_Profile, name="List_Profile"),
    path('pro/', create_profile),
    path('pro/<int:profile_id>/', update_profile),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
