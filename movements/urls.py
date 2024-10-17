from django.urls import path
from . import views

urlpatterns = [
    # Products Entries URLs
    path(
        "products_entries/",
        views.ProductEntryListCreateApiView.as_view(),
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
        views.StockEntryListCreateApiView.as_view(),
        name="stocks_entries-list-create",
    ),
    path(
        "stocks_entries/<int:pk>/",
        views.StockEntryRetrieveUpdateDestroyApiView.as_view(),
        name="stocks_entries-retrieve-update-destroy",
    ),
    # Sotcks Outs URLs
    path(
        "stocks_outs/",
        views.StockOutListCreateApiView.as_view(),
        name="stocks_entries-list-create",
    ),
    path(
        "stocks_outs/<int:pk>/",
        views.StockOutRetrieveUpdateDestroyApiView.as_view(),
        name="stocks_entries-retrieve-update-destroy",
    ),

    # Total Stocks URLs
    path("stocks/<int:pk>/", views.StockView.as_view(), name="stock")
]
