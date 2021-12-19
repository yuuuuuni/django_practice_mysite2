from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), # pybo/ url이 요청되면 pybo의 urls의 매핑 정보를 읽어서 처리하라는 의미
]
