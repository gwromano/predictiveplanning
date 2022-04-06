from django.urls import path, include

from django.views.generic import TemplateView

from django.contrib import admin
import urllib3

admin.autodiscover()

import hello.views


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    urllib3(r'profile/',hello.views,name="profile")

]
