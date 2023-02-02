from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
import users.urls as users_urls
from Capstone_Project2.views import AccountViewSet,GenreViewSet,ItemViewSet,RecordViewSet, FriendsViewSet, FriendRequestViewSet
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'Account', AccountViewSet)
router.register(r'Item', ItemViewSet)
router.register(r'Record', RecordViewSet)
router.register(r'Genres', GenreViewSet)
router.register(r'Friends', FriendsViewSet)
router.register(r'FriendRequest', FriendRequestViewSet)


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^docs/',include_docs_urls(title="墨瓣后台，闲人免进")),
]

urlpatterns += users_urls.urlpatterns