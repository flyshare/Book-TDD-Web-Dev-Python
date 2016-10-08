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
    
)
