from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from Inventory.views import DrugTypeViewSet, StockViewSet
from Inventory.views.item_viewset import ItemViewSet

router = SimpleRouter()
router.register(r'drug_types', DrugTypeViewSet)
router.register(r'stock', StockViewSet)
router.register(r'catalog_item', ItemViewSet)

urlpatterns = [
    url('', include(router.urls)),
]
