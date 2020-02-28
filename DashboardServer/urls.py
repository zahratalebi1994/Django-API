from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.views import AttacksViewSet

# letting urls work with or without / at the end
router = routers.DefaultRouter(trailing_slash=False)

# adding point routes
router.register('attacks', AttacksViewSet)
# router.register('point-ranges', PointRangeViewSet, base_name='point-range')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]