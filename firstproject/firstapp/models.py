from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class project(models.Model):
    name = models.CharField(max_length = 100)
    users = models.ManyToManyField(person)
    def __str__(self):
        return self.name

class project_user(models.Model):
    p_id = models.ForeignKey(project, on_delete= models.CASCADE)
    u_id = models.ForeignKey(person, on_delete=models.CASCADE)
    is_mentor = models.BooleanField(default= False)

