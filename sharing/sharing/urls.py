"""sharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include  #url 상속
# from backend import views
from django.views.generic import TemplateView #templateview 상속
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/',include('backend.urls')),
    #auth 관련 url
    
    # POST 방식으로 username, password 를 포함한 token 획득
    path('login/', obtain_jwt_token),   
    # 일반적으로 서비스가 사용자로부터 받은 JWT를 인증 서비스로 전달하여 JWT가 유효한지 확인한 후 사용자에게 보호된 리소스를 반환함을 의미
    path('verify/', verify_jwt_token),  
    #  'JWT_ALLOW_REFRESH': True 로 settings 에 준 옵션 때문에 만료 되지 않은 토큰도 만료 시간 갱신된 새로운 토큰 발급 가능
    path('refresh/', refresh_jwt_token), 
    #accounts 앱에 있는 url 상속
    path('accounts/', include('accounts.urls')),
    # 프론트의 index 를 띄우는 url ( 저번 포스팅 참고 )
    path('', TemplateView.as_view(template_name='index.html')),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

