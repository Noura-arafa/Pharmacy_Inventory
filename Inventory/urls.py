from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from Inventory.views import DrugTypeViewSet

router = SimpleRouter()
router.register(r'drug_types', DrugTypeViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
