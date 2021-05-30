from .models import Post,Category
from rest_framework import serializers
from accounts.serializers import ProfileSerializer



class PostSerializer(serializers.ModelSerializer):
    #forienkey 로 연결된 필드는 관계를 명시할 때 read_only=True 를 쓴다.
    #다대다 관계는 many=True.
    user = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['user','id','category','image','title','content','url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']