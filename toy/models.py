from django.db import models

class Toy(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, default="")
    category = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField(blank=True, null=True)
    was_included_in_home = models.BooleanField()
    class Meta:
        ordering = ('created',)
        indexes = [
           models.Index(fields=("created",))
        ]   
    def __str__(self):
           return self.name