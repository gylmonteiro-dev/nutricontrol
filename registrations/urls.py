from django.urls import path
from . import views

urlpatterns = [
    # Products URLs
    path(
        "products/",
        views.ProductListCreateApiView.as_view(),
        name="product-list-create",
    ),
    path(
        "products/<int:pk>/",
        views.ProductRetrieveUpdateDestroyApiView.as_view(),
        name="product-retrieve-update-destroy",
    ),
    # Places URLs
    path(
        "places/",
        views.PlaceListCreateApiView.as_view(),
        name="place-list-create",
    ),
    path(
        "places/<int:pk>/",
        views.PlaceRetrieveUpdateDestroyApiView.as_view(),
        name="place-retrieve-update-destroy",
    ),
    # Suppliers URLs
    path(
        "suppliers/",
        views.SupplierListCreateApiView.as_view(),
        name="supplier-list-create",
    ),
    path(
        "suppliers/<int:pk>/",
        views.SupplierRetrieveUpdateDestroyApiView.as_view(),
        name="supplier-retrieve-update-destroy",
    ),
]
