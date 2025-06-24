from rest_framework import routers
from .views import CustomUserViewset

router = routers.DefaultRouter()
router.register(r"users", CustomUserViewset, basename="customuser")


urlpatterns = router.urls
