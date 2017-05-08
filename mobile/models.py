from django.db import models


# Create your models here.

class users(models.Model):
    GENDERCHOICE = (
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Rather Not Say'),
    )
    USERACTIVE = (
        (0, 'InActive'),
        (1, 'Active'),
    )

    uid = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERCHOICE, default=0)
    dob = models.DateField(max_length=50, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    bio = models.CharField(max_length=100, blank=True, null=True)
    join_date = models.DateTimeField(max_length=50, blank=True, null=True)
    total_views = models.IntegerField(default=0, blank=True, null=True)
    profile_pic = models.CharField(max_length=1000, default='', blank=True, null=True)
    is_active = models.CharField(max_length=1, choices=USERACTIVE, default=1)


class InterestsContent(models.Model):
    name = models.CharField(max_length=300, default='', blank=True, null=True)
    image = models.CharField(max_length=1000, default='', blank=True, null=True)
    creation_date = models.DateTimeField()


class Interests(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    interest_content = models.CharField(max_length=200, default='',null=True)
    # interest_content = models.ForeignKey(InterestsContent, on_delete=models.CASCADE, blank=True)

class Post(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default='', blank=True,null=True)
    tag = models.CharField(max_length=500, default='', blank=True,null=True)
    interest = models.ForeignKey(InterestsContent, default='')
    # views = models.CharField() make foreign key as varchar so that can add user id with comma sepration
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', null=True, max_length=255)

    creation_date = models.DateTimeField(auto_now=True) #use str(datetime.datetime.now())[:19] while retreiving

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, default='', blank=True,null=True)
    creation_date = models.DateTimeField(auto_now=True) #use str(datetime.datetime.now())[:19] while retreiving
    updatation_date = models.DateTimeField(null=True,blank=True)
