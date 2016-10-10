from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       # Examples:

                       # url(r'^$', 'superlists.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # include() 表示把此 url映射 让引入另一个 urls 来映射
                       # url(r'^admin/', include(admin.site.urls)),
                       # '$' 表示空字符
                       url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
                       url(r'^new$', 'lists.views.new_list', name='new_list'),
                       url(r'^(\d+)/add_item$',
                           'lists.views.add_item', name='add_item'),
                       )
