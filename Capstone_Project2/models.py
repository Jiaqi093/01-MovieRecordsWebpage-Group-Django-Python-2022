from django.db import models
import uuid
from enumchoicefield import EnumChoiceField, ChoiceEnum
from users.models import User


class item_type(ChoiceEnum):
    play = "play"
    movie = "movie"
    tv_show = "TV show"
    book = "book"
    music = "music"
    other = "other"
class privacy(ChoiceEnum):
    private = "private"
    public = "public"
    friend_only = "friend only"

class gender(ChoiceEnum):
    male = "male"
    female = "female"
    other = "other"


class Account(models.Model):
    account_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    birthday = models.DateTimeField(null=True)
    profile = models.ImageField(null=True)
    friend = models.FileField(null=True)
    is_delete =models.BooleanField(default=True,null=False)

class Item(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    type = EnumChoiceField(enum_class=item_type , default=None)
    publish_date = models.DateTimeField(null=True)
    name = models.CharField(max_length=50, null=False, unique=True)
    author = models.CharField(max_length=50, null=False, unique=True)
    image = models.ImageField(upload_to='photos', max_length=255, null=True)
    num_records = models.IntegerField(null=True)
    top_10_tags = models.FileField(null=True)
    comment = models.TextField(null=True)
    is_delete = models.BooleanField(default=True, null=False)


class Genres(models.Model):
    genre = models.CharField(max_length=50, unique=True)


class Records(models.Model):
    records_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    item = models.CharField(max_length=50,null=True)
    title = models.CharField(max_length=50, null=False)
    artist = models.CharField(max_length=50, null=False)
    genres = models.ManyToManyField(Genres, related_name="myGenres")
    publish_date = models.DateTimeField(null=True)
    if_complete = models.BooleanField(null=True)
    comment = models.TextField(null=True)
    rate = models.FloatField(null=True)
    tag = models.CharField(max_length=25,null=True)
    like = models.IntegerField(null=True)
    othercomment = models.FileField(null=True)
    privacy = EnumChoiceField(enum_class=privacy , default=privacy.private)
    is_delete = models.BooleanField(default=True, null=False)
    thumbnail = models.ImageField(upload_to = 'capstone_project_vue/src/assets', null = True)


class Friends(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name = "account")
    friends = models.ManyToManyField(Account, blank=True, related_name = "friends")

    def __str__(self):
        return self.account.account_id

    # add the account into the target friend list
    def add_friend(self, account):
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()

    # helper function for delete friend
    def remove_friend(self, account):
        if account in self.friend.all():
            self.friends.remove(account)

    # remove the account from the target friend list
    def delete_friend(self, removee):
        remover_friend_list = self
        remover_friend_list.remove_friend(removee)

        removee_friend_list = Friends.objects.get(user = removee)
        removee_friend_list.remove_friend(self.account)


class FriendRequest(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name = "sender")
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name = "receiver")
    is_friend_request = models.BooleanField(blank = True, null = False, default = True)
    is_accepted = models.BooleanField(null=False, default = False)
    request_Time = models.DateTimeField(null=True)

    # Both senders and receivers will add each other to their friend list. Then close the friend request window.
    def accept_friend(self):
        receiver_friend_list = Friends.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = Friends.objects.get(self.receiver)
            if sender_friend_list:
                sender_friend_list.add_friend(self.sender)
                self.is_friend_request = False
                self.save()

    # decline the friend request by close the friend request window.
    def decline_friend(self):
        self.is_friend_request = False
        self.save()

