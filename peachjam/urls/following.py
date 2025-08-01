from django.urls import path

from peachjam.views import (
    UserFollowingButtonView,
    UserFollowingCreateView,
    UserFollowingDeleteView,
)

urlpatterns = [
    path(
        "button/",
        UserFollowingButtonView.as_view(),
        name="user_following_button",
    ),
    path(
        "create/",
        UserFollowingCreateView.as_view(),
        name="user_following_create",
    ),
    path(
        "<int:pk>/delete/",
        UserFollowingDeleteView.as_view(),
        name="user_following_delete",
    ),
]
