'''
Views for Recipe APIs.
'''
from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
)
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    '''Manage recipes in the database.'''
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        '''Retrieve recipes for authenticated user.'''
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        '''Return appropriate serializer class.'''
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        '''Create a new recipe.'''
        serializer.save(user=self.request.user)

class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''Manage tags in the database.'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        '''Retrieve tags for authenticated user.'''
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def get_serializer_class(self):
        '''Return appropriate serializer class.'''
        if self.action == 'list':
            return serializers.TagSerializer
        return self.serializer_class