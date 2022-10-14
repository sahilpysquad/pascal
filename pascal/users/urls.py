from django.urls import path

from pascal.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    DepartmentView
)

app_name = "users"
urlpatterns = [
    path("department/", view=DepartmentView.as_view(), name="add_department"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
