from django.db import models

STATUS_CHOICES = [('Not Started','Not Started'),('In Progress','In Progress'),('Completed','Completed'),('On Hold','On Hold')]

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    brief = models.TextField(blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Not Started')
    start_date = models.DateField(null=True, blank=True)
    aircraft = models.CharField(max_length=120, blank=True)
    no_meetings = models.PositiveIntegerField(default=0)
    iom_tm = models.PositiveIntegerField(default=0)
    no_sorties = models.PositiveIntegerField(default=0)
    trials = models.PositiveIntegerField(default=0)
    end_date = models.DateField(null=True, blank=True)
    miscellaneous_reason = models.TextField(blank=True, null=True)
    marked_reason = models.TextField(blank=True, null=True)
    marked_by = models.CharField(max_length=120, blank=True, null=True)
    attachment = models.FileField(upload_to='project_docs/', blank=True, null=True)
    

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.project_name} ({self.status})"
    
    
class Project(models.Model):
    ...
    document = models.FileField(
        upload_to='documents/',
        blank=True,
        null=True
    )
