from django.urls import path

import webapp.views.base

urlpatterns = [
    path("", webapp.views.base.home_view),
]

