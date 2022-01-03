from django.db import models


class Poll(models.Model):
    question = models.TextField()
    first_option = models.CharField(max_length=30)
    second_option = models.CharField(max_length=30)
    third_option = models.CharField(max_length=30)
    first_count = models.IntegerField(default=0)
    second_count = models.IntegerField(default=0)
    third_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def total(self):
        return self.first_count + self.second_count + self.third_count
