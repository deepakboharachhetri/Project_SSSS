from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.utils import timezone


User = settings.AUTH_USER_MODEL

# Create your models here.
# swiper model

TYPE_CHOICES =(
    ("admin","admin") ,
    ("moderator","moderator")
)

STATUS_CHOICES={
    ("active","active"),
    ("inactive","inactive")
}


class CostumUser(AbstractUser):
    userid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=40,unique=True,validators=[
            MinLengthValidator(8, 'the field must contain at least 8 characters')
            ])
    category=models.CharField(max_length=10,choices=TYPE_CHOICES)
    email=models.EmailField(max_length=200)
    status=models.BooleanField(default=True)
    USERNAME_FIELD='username'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS=['category','email']
    class Meta:
        ordering=['userid']
    def __str__(self) :
        return self.username

class HomeSwiper(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    position =models.IntegerField(unique=True)
    title=models.CharField(max_length=60)
    desc=models.CharField(max_length=150)
    img=models.ImageField(upload_to='swiper/')
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta:
        ordering=['status']
    def __str__(self):
        return self.title

class Achievement(models.Model):
    id = models.AutoField(primary_key=True)
    year_of_experiences=models.IntegerField(unique=True)
    teacher_no=models.IntegerField()
    bright_students=models.IntegerField(unique=True)
    glorious_alumini=models.IntegerField(unique=True)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta:
        ordering=['first_upload_date']

class Introduction(models.Model):
    id = models.AutoField(primary_key=True)
    firstpara=models.CharField(max_length=1000)
    secondpara=models.CharField(max_length=2000)
    thirdpara=models.CharField(max_length=1000)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']

# about section modelsC:\Users\hello_world\Desktop\test\Shree Sarbajanik\schoolproject\schoolproject\urls.py
    
#about vision model
class AboutVision(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    firstpara=models.CharField(max_length=1000)
    secondpara=models.CharField(max_length=2000)
    thirdpara=models.CharField(max_length=1000)
    fourthpara=models.CharField(max_length=1000)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    
    def __str__(self):
        return self.firstpara

#abou principle model
class AboutPrinciple(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    principleintro=models.CharField(max_length=200)
    img=models.ImageField(upload_to='principleimg/')
    firstpara=models.CharField(max_length=1000)
    secondpara=models.CharField(max_length=2000)
    thirdpara=models.CharField(max_length=1000)
    fourthpara=models.CharField(max_length=1000)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.firstpara
    
# about history model
class AboutHistory(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    firstpara=models.CharField(max_length=1000)
    secondpara=models.CharField(max_length=2000)
    thirdpara=models.CharField(max_length=1000)
    fourthpara=models.CharField(max_length=1000)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.firstpara


# notice models
class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    file1=models.FileField(upload_to='Notice/img')
    title2=models.CharField(max_length=200,default=None)
    file2=models.FileField(upload_to='Notice/',default=None)
    title3=models.CharField(max_length=200,default=None)
    file3=models.FileField(upload_to='Notice/',default=None)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.title


# gallery model
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery/')
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.title


# more document model
class MoreDoc(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='moredocument/')
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.title
    
# samachar model
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    link=models.URLField(max_length=300)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.title
    

class Social(models.Model):
    id = models.AutoField(primary_key=True)
    facebook=models.URLField(max_length=300)
    twitter=models.URLField(max_length=300)
    linkedin=models.URLField(max_length=300)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.facebook

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    location=models.URLField(max_length=1000)
    gmail_api=models.URLField(max_length=300)
    gmail=models.EmailField(max_length=300)
    phn_no=models.CharField(max_length=10)
    uploadby=models.ForeignKey(CostumUser,on_delete=models.CASCADE)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return self.phn_no





class  User_profile(models.Model):
    profile_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=40,unique=True)
    userid=models.ForeignKey(CostumUser,null=True,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=40)
    middle_name=models.CharField(max_length=40,blank=True)
    last_name=models.CharField(max_length=40)
    img=models.ImageField(upload_to='profile/')
    phn_no=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    status=models.CharField(max_length=8,default='active',choices=STATUS_CHOICES)
    first_upload_date=models.DateTimeField(default=timezone.now())
    updateDate=models.DateTimeField(null=True,blank=True)
    lastDate=models.DateTimeField(null=True,blank=True)
    class Meta :
        ordering=['first_upload_date']
    def __str__(self):
        return str(self.first_name+" "+self.middle_name+" "+self.last_name)
    

    
class ProvinceInformation(models.Model):
  id=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=100)
  class Meta:
      ordering=['name']
  def __str__(self):
      return self.name

class DistrictInformation(models.Model):
  id=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=100)
  pro_id=models.ForeignKey(ProvinceInformation,on_delete=models.PROTECT)
  class Meta:
      ordering=['name']
  def __str__(self):
      return self.name

class MunicipalityInformation(models.Model):
  id=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=200)
  pro_id=models.ForeignKey(ProvinceInformation,on_delete=models.PROTECT)
  dist_id=models.ForeignKey(DistrictInformation,on_delete=models.PROTECT)
  class Meta:
      ordering=['name']
  def __str__(self):
      return self.name


