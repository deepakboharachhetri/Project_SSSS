
from django import forms
from adminap.models import *

# swiper form
class HomeSwiperForm(forms.Form):
    class Meta:
        model=HomeSwiper
        fields=['position','title','desc','img','uploadby']

#about form 
class AboutVisionForm(forms.Form):
    class Meta:
        model=AboutVision
        fields=['auto_increment_id','firstpara','secondpara','thirdpara','fourthpara','uploadby','updateDate']
class AboutPrincipleForm(forms.Form):
    class Meta:
        model=AboutPrinciple
        fields=['auto_increment_id','title','principleintro','img','firstpara','secondpara','thirdpara','fourthpara','uploadby','updateDate']
class AboutHistoryForm(forms.Form):
    class Meta:
        model=AboutHistory
        fields=['auto_increment_id','firstpara','secondpara','thirdpara','fourthpara','uploadby','updateDate']

# notice form
class NoticeForm(forms.Form):
    class Meta:
        model=Notice
        fields=['id','title','description','file1','title2','file2','title3','file3','uploadby','updateDate']

# gallery form
class GalleryForm(forms.Form):
    class Meta:
        model=Gallery
        fields=['id','title','img','uploadby','updateDate']

# more form
class MoreForm(forms.Form):
    class Meta:
        model=MoreDoc
        fields=['id','title','file','uploadby','updateDate']

# news form
class NewsForm(forms.Form):
    class Meta:
        model=News
        fields=['id','title','link','uploadby','updateDate']

# social form
class SocialForm(forms.Form):
    class Meta:
        model=Social
        fields=['id','facebook','twitter','linkedin','uploadby','updateDate']
class ContactForm(forms.Form):
    class Meta:
        model=Contact
        fields=['id','location','gmail_api','gmail','phn_no','uploadby','updateDate']

class AchievementForm(forms.Form):
    class Meta:
        model=Achievement
        fields=['id','year_of_experiences','teacher_no',' bright_students',' glorious_alumini','uploadby','updateDate']

class IntroductionForm(forms.Form):
    class Meta:
        model=Introduction
        fields=['id','firstpara','secondpara','thirdpara','uploadby','updateDate']


# class ModeratorForm(forms.Form):
#     class Meta:
#         model=Introduction
#         fields=['username','user','first_name','middle_name','last_name','img','phn_no','address']
class User_profileForm(forms.Form):
    class Meta:
        model=Introduction
        fields=['userid','username','user','first_name','middle_name','last_name','img','phn_no','post','bio']
class CostumUserForm(forms.Form):
    class Meta:
        model=CostumUser
        fields=['username','password','category','email']

