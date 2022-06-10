from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Message(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.content
