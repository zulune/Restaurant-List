from django.contrib.auth import get_user_model

User = get_user_model()

random_ = User.objects.last()

# My followers
random_.profile.followers.all()

# Who i following
random_.profile.following.all()
