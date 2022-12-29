'''
Serializers for Recipe APIs.
'''
from rest_framework import serializers

from core.models import Recipe, Tag

class TagSerializer(serializers.ModelSerializer):
    '''Serializer for Tag objects.'''

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

class RecipeSerializer(serializers.ModelSerializer):
    '''Serializer for Recipe objects.'''
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'time_minutes',
            'price',
            'link',
            'tags',
        ]
        read_only_fields = ['id']

class RecipeDetailSerializer(RecipeSerializer):
    '''Serializer for recipe detail view.'''

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
