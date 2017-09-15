from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
<link rel = "shortcuticon" herf="/favicon.ico"/>

# 파이썬에서는 정규 표현식을 작성할 때 항상 문자열 앞에 r을 붙인다.
# 파이썬에게 문자열에 특수 문자가 있다는 것을 알려줌.
