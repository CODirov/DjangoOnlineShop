from django.db import models


class Rank(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    fullname = models.CharField(max_length=255)
    about = models.TextField()
    image = models.ImageField(upload_to="images/")
    date_of_birth = models.CharField(max_length=255)

    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname