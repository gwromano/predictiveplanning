from django.urls import path, include

from django.views.generic import TemplateView

from django.contrib import admin

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
    path("accounts/", TemplateView.as_view(template_name='login.html'),
                        include("django.contrib.auth.urls")),
    path("about-us/", TemplateView.as_view(template_name='about-us.html'),
                      name='about-us'),
    path("make-order/", TemplateView.as_view(template_name='make-order.html'),
                      name='make-order'),
    path("order-history/", TemplateView.as_view(template_name='order-history.html'),
                      name='order-history'),
    

]
