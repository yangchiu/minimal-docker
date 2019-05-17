from django.db import models

class Item(models.Model):
    process_time = models.IntegerField()
    
    def __str__(self):
        return 'item-(' + str(self.process_time) + ')'
