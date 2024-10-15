from django.urls import path
from . import views

urlpatterns = [
    # Products Entries URLs
    path(
        "products_entries/",
        views.ProductEntryLisctCreateApiView.as_view(),
        name="products_entries-list-create",
    ),
    path(
        "products_entries/<int:pk>/",
        views.ProductEntryRetrieveUpdateDestroyApiView.as_view(),
        name="products_entries-retrieve-update-destroy",
    ),
    # Sotcks Entries URLs
    path(
        "stocks_entries/",
        views.StockEntryLisctCreateApiView.as_view(),
        name="stocks_entries-list-create",
    ),
    path(
        "stocks_entries/<int:pk>/",
        views.ProductEntryRetrieveUpdateDestroyApiView.as_view(),
        name="stocks_entries-retrieve-update-destroy",
    ),
]
