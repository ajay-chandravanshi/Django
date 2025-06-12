from rest_framework import routers
from .views import StudentViewSets

router = routers.SimpleRouter()
router.register(r'users', StudentViewSets)
urlpatterns = router.urls