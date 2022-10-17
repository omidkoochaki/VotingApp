from rest_framework import routers

from posts.views import PostViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register(prefix='', viewset=PostViewSet, basename='posts')
post_urls = router.urls

votes_router = routers.DefaultRouter()
votes_router.register(prefix='', viewset=VoteViewSet, basename='tasks')
votes_urls = votes_router.urls


