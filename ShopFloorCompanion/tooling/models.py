from django.db import models

class ToolOrder(models.Model):
    name = models.CharField(max_length=50)
    part_num = models.CharField(max_length=25)
    machine_num = models.CharField(max_length=5)
    needed = models.DateTimeField()
    tools = models.TextField()
    comments = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return 'ID: ' + str(self.id) + ' Machine: ' + self.machine_num
