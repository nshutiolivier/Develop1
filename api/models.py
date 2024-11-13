from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=244)
    last_name = models.CharField(max_length=244)
    age = models.IntegerField()

    def __str__(self):
        return f" {self.last_name} {self.first_name}"


class Author(models.Model):
    name = models.CharField(max_length=244)
    bio = models.CharField(max_length=244)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=244)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(default='2024-01-01')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=244)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
