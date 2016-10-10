from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:

                       # url(r'^$', 'superlists.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # include() 表示把此 url映射 让引入另一个 urls 来映射
                       # url(r'^admin/', include(admin.site.urls)),
                       # '$' 表示空字符
                       url(r'^$', 'lists.views.home_page', name='home_page'),
                       url(r'^lists/(\d+)/$',
                           'lists.views.view_list', name='view_list'),
                       url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
                       url(r'^lists/(\d+)/add_item$',
                           'lists.views.add_item', name='add_item'),
                       )
