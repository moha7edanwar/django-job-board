from django.db import models
from django.utils.text import slugify
# Create your models here.

JOB_TYPE=[
    ('part-time','part-time'),
    ('full-time','full-time')
]

class job(models.Model):
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