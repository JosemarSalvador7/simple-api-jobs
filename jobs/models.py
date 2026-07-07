from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary= models.DecimalField(max_digits=12,decimal_places=2)
    skills = models.ManyToManyField('skills.Skill',related_name='jobs')
    
    def __str__(self):
        return self.title 
    
    def __repr__(self) -> str:
        return f'<Jobs>  {self.title}'
    