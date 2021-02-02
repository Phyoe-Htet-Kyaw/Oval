from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=255, null=False)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)
    nrc_passport = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=15, null=True)
    studentID = models.CharField(max_length=20, null=True)
    university = models.ForeignKey('University', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
    major = models.ForeignKey('Major', on_delete=models.CASCADE, null=True)
    academic_year = models.CharField(max_length=10, null=True)
    profile_picture = models.CharField(max_length=255, null=True)
    cover_photo = models.CharField(max_length=255, null=True)
    user_role = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

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