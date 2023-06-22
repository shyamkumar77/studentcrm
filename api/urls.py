from django.urls import path

from api.views import StudentsView

from rest_framework.routers import DefaultRouter #using DefaultRouter bcoz used modelviewset
router=DefaultRouter()
router.register("students",StudentsView,basename="students")

urlpatterns = [

]+router.urls