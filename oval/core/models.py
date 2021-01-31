from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    nrc_passport = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    studentID = models.CharField(max_length=20)
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=10)
    profile_picture = models.CharField(max_length=255)
    cover_photo = models.CharField(max_length=255)
    user_role = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    city_id = models.IntegerField()
    country_id = models.IntegerField()
    profile_picture = models.CharField(max_length=255)
    cover_photo = models.CharField(max_length=255)
    representative_id = models.IntegerField()
    description = models.TextField()
    major_id = models.IntegerField()
    google_map_link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    description = models.TextField()
    post_type_id = models.IntegerField()
    user_id = models.IntegerField()
    university_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PostType(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AskQuestion(models.Model):
    description = models.TextField()
    user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)