from django.urls import path

from pascal.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    department_add_view
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
path("~department/", view=department_add_view, name="add-department"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
