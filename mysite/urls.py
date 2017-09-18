from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views # 추가


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'), # 추가
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}), # 추가
    url(r'', include('blog.urls')),
]


# 파이썬에서는 정규 표현식을 작성할 때 항상 문자열 앞에 r을 붙인다.
# 파이썬에게 문자열에 특수 문자가 있다는 것을 알려줌.
