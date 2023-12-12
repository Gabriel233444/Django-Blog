from rest_framework import serializers    
from .models import Post, Comment

post = Post
comment = Comment

class PostListSerializer(serializers.ModelSerializer):
    """ Serializers for Listing Posts """
    
    class Meta:
        fields = "__all__"
        model = post
        
class CommentListSerializer(serializers.ModelSerializer):
    """ Serializers for Listing Comments """
    
    class Meta:
        fields = "__all__"
        model = comment
        
       
class PostCreateSerializer(serializers.ModelSerializer):
    """ Serializers for Creating Images """
    
    class Meta:
        fields = ['id', 'title', 'slug', 'author', 'updated_on', 'content', 'created_on', 'status', 'image']
        model = post
        
class CommentCreateSerializer(serializers.ModelSerializer):
    """ Serializers for Listing Comments """
    
    class Meta:
        fields = ['id', 'post', 'name', 'email', 'body', 'created_on', 'active']
        model = comment
        
        
class PostUpdateSerializer(serializers.ModelSerializer):
    """ Serializers for updating Images """
    
    class Meta:
        fields = ['id', 'title', 'slug', 'author', 'updated_on', 'content', 'created_on', 'status']
        model = post
        
class CommentUpdateSerializer(serializers.ModelSerializer):
    """ Serializers for updating Images """
    
    class Meta:
        fields = ['id', 'post', 'name', 'email', 'body', 'created_on', 'active']
        model = comment
        
        
class PostDestroySerializer(serializers.ModelSerializer):
    """ Serializers for Deleting Images """
    
    class Meta:
        fields = "__all__"
        model = post
        
class CommentDestroySerializer(serializers.ModelSerializer):
    """ Serializers for Deleting Images """
    
    class Meta:
        fields = "__all__"
        model = comment
        
