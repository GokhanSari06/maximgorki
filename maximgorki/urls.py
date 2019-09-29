from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from blog import views as blog_views
from hakkimizda import views as hakkimizda_views
from hizmetlerimiz import views as hizmetlerimiz_views
from portfolyo import views as portfolyo_views



admin.site.site_header = "Maxim Gorki"
admin.site.site_title = "Panel"
admin.site.index_title = "Maxim Gorki | Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('hakkimizda/', include('hakkimizda.urls')),
    path('hizmetlerimiz/', include('hizmetlerimiz.urls')),
    path('portfolyo/', include('portfolyo.urls')),
    path('', views.index),
    path('', blog_views.blog_listesi),
    path('', hakkimizda_views.hakkimizda_listesi),
    path('', hizmetlerimiz_views.hizmetlerimiz_listesi),
    path('', portfolyo_views.portfolyo_listesi),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)