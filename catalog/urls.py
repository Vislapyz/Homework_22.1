from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, product_detail, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    # path('base/', HomePageView.as_view(), name='base'),

    path('', ProductListView.as_view(), name='products'),
    path("products/<int:pk>/", product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts')
]