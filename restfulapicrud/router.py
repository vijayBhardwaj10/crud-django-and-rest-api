from django.db import router
from employeeapi.viewsets import employeeviewset
from rest_framwork import routers

router = routers.DefaultRouter()
router.register('employee',employeeviewset)