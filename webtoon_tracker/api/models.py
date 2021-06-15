from django.db import models

class Webtoon(models.Model):
    title = models.CharField(max_length=200, unique=True)
    dropped = models.BooleanField(default=False)
    completed_reading = models.BooleanField(default=False)
    authors = models.ManyToManyField('Author', related_name='authors')
    days_of_release = models.ManyToManyField('DayOfRelease', related_name='days_of_release')

    def __str__(self):
        return self.title

class Author(models.Model):
    username = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.username

class DayOfRelease(models.Model):
    DAY_OF_WEEK = [
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THUR', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    ]
    day_of_week = models.CharField(max_length=4, choices=DAY_OF_WEEK, default='SUN', unique=True)

    def __str__(self):
        return self.day_of_week