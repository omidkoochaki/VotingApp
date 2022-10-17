from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Vote
from posts.serializers import PostSerializer, VoteSerializer, CreatePostSerializer


class PostViewSet(ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePostSerializer
        else:
            return PostSerializer


class VoteViewSet(ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = VoteSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        post = Post.objects.filter(id=self.kwargs.get('post_id'))
        if post:
            context.update({
                'post': post[0]
            })
        else:
            raise NotFound(detail=None, code=None)
        return context

    def get_queryset(self):

        post_id = self.kwargs.get('post_id')
        return Vote.objects.filter(post__id=post_id)
