from mobile.models import users


class UserSerializer:
    class Meta():
        model = users;
        fields = ('uid','first_name','last_name','email','profile_pic','gender')
