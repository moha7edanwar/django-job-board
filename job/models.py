from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

JOB_TYPE=[
    ('part-time','part-time'),
    ('full-time','full-time')
]

class job(models.Model):
    owner = models.ForeignKey(User , related_name= 'job_owner' , on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    job_type = models.CharField(max_length=25  ,choices = JOB_TYPE)
    description = models.CharField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category' ,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='jobs/')
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args , **kwargs):
        self.slug= slugify(self.title)
        super(job,self).save(*args,**kwargs)


    def __str__(self):
        return self.title
    



class category(models.Model):
    name =models.CharField(max_length=25)




    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(job , related_name= 'apply_job' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=500)
    website = models.URLField (max_length=500)
    cv = models.FileField(upload_to='job/files')
    coverliter = models.TextField()

    def __str__(self):
        return self.name 
    
