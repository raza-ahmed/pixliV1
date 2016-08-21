from __future__ import unicode_literals
from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length= 300, default="pixli")
    event_code = models.CharField(max_length=250, default="pixlicode")
    event_cover = models.CharField(max_length=1000, default="defaultcover")
    event_date = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=200, default="wedding and tour")


    def __str__(self):
        return self.event_name+' - '+self.event_type

class Photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default="pixli_pic")
    caption = models.CharField(max_length=200, default="pixli_pic_caption")
    photo_source = models.CharField(max_length=1000, default='pixli_pic_url')
    photo_likes = models.PositiveIntegerField(default=0)
    photo_share = models.PositiveIntegerField(default=0)