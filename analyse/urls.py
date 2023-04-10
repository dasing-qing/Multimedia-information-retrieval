from django.conf.urls import url

from .views import index, file,theme,  a

urlpatterns = [


    url(r'^a/$', a),

    url(r'^file/$', file),


    url(r'^theme/$', theme),

    url(r'^$', index),

]
