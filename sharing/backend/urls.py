from .models import *
from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet,CategoryViewSet


# #router 방법



# router = routers.DefaultRouter()  # DefaultRouter 설정
# router.register('users', UserViewSet)  # ViewSet과 함께 users라는 router 등록


#Create,Read
post_list = PostViewSet.as_view({
    'post': 'create',
    'get': 'list'
})
#Update,Delete
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

category_list = CategoryViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = ([
    #위 라우터의 urls을 include
    # path('', include(router.urls)),
    #위에서 적어준 url 로 각각 매핑
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('categories/',category_list,name="category_list"),
    path('categories/<int:pk>',category_detail,name="category_detail")
])
