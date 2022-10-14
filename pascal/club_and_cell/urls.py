from django.urls import path

from pascal.club_and_cell.views import ClubCellView, ClubCellListView

app_name = "club_and_cell"
urlpatterns = [
    path("create/", ClubCellView.as_view(), name="create_club_cell"),
    path("all-clubs-and-cells/", ClubCellListView.as_view(), name="all_clubs_and_cells")
]
