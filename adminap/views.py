from django.shortcuts import render,redirect
import datetime
# Create your views here.

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
# from schoolap.views import updater_data
from schoolap.models import ViewerContacts
from adminap.models import *
from adminap.forms import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import exceptions
import os
from django.utils import timezone
# Create your views here.


# *****admin panels*****

# admin dashboard

@login_required(login_url='/Admin/')
def AdminPanelHome(request):
#  admin=Admin.objects.filter(username=username)
 data={
    "updater":request.user.username,
    'category':request.user.category,
 }
 return render(request,'AdminpanelHome.html',data)

# admin swiper 
@login_required(login_url='/Admin/')
def AdminPanelHomeSwiperView(request):
       form=HomeSwiper.objects.all().filter(status='active').order_by('position')
       data={
         'updater':request.user.username,
         'form':form,
         'category':request.user.category,
         }
       return render(request,'AdminPanelHomeSwiperView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelHomeSwiperAdd(request):
   if(request.method=='POST'):
       form=HomeSwiperForm(request.POST,request.FILES) 
       title=request.POST.get('edit_swiper_title')
       position=request.POST.get('edit_swiper_position')
       desc=request.POST.get('edit_swiper_description')
       i=request.FILES.get('edit_swiper_image') 
       Costum=CostumUser.objects.get(username=request.user.username)
       
       home=HomeSwiper(
          title=title,
          desc=desc,
          position=int(position),
          img=i,
          uploadby=Costum,
          
          )
       home.save()
       return redirect('AdminPanelHomeSwiperView')
   
   arr=[1,2,3,4,5,6,7,8,9]
   positionfull=HomeSwiper.objects.values_list('position',flat=True)

   data={
          'updater':request.user.username,
          'arr':arr,
         'occupied':positionfull,
          }
   return render(request,'AdminPanelHomeSwiper.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelHomeSwiperEdit(request,id):
   if(request.method=='POST'):
       form=HomeSwiperForm(request.POST,request.FILES) 
       title=request.POST.get('edit_swiper_title')
       position=request.POST.get('edit_swiper_position')
       desc=request.POST.get('edit_swiper_description')
       i=request.FILES.get('edit_swiper_image') 
       postimg=HomeSwiper.objects.get(id=id).img
       
       if type(i)==None:
          i=i
       else:
          i=postimg
       HomeSwiper.objects.filter(id=id).update(
          title=title,
          desc=desc,
          position=int(position),
          img=i,
          uploadby=CostumUser.objects.get(username=request.user.username),
          updateDate=timezone.now()    )

       
       return redirect('AdminPanelHomeSwiperView')
   arr=[1,2,3,4,5,6,7,8,9]
   form=HomeSwiper.objects.get(id=id)
   positionfull=HomeSwiper.objects.values_list('position',flat=True)
   data={
          'updater':request.user.username,
          'arr':arr,
          'form':form,
          'occupied':positionfull
          }
   return render(request,'AdminPanelHomeSwiper.html',data) 

# MyModel.objects.filter(pk=some_value).update(field1='some value')

@login_required(login_url='/Admin/')
def deleteswiper(request,pk):
   form=HomeSwiper.objects.filter(id=pk)
   form.delete()
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelHomeSwiperView')




# school achievement
@login_required(login_url='/Admin/')
def AdminPanelAchievementView(request):
   form=Achievement.objects.all().filter(status='active')
   data={
      "form":form,
      "updater":request.user.username,
      'category':request.user.category,
   }
   return render(request,
   'AdminPanelAchievementView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelAchievementAdd(request):
    form_id=Achievement.objects.filter(status='active')
    if(request.method=='POST'):
      form=AchievementForm(request.POST)
      experience_year=request.POST.get('experience_year')
      teacher_no=request.POST.get('teacher_no')
      bright_students=request.POST.get('bright_students')
      glorious_alumini=request.POST.get('glorious_alumini')
      uploadby=CostumUser.objects.get(username=request.user.username)
      form=Achievement(
          year_of_experiences=experience_year,
          teacher_no=teacher_no,
          bright_students=bright_students,
          glorious_alumini=glorious_alumini,
          uploadby=uploadby
       )
      form.save()
      messages.info(request,"Add successfully ")
      form_id=form_id.values_list('id',flat=True)
      for x in form_id:
         Achievement.objects.filter(id=x).update(status='inactive',lastDate=timezone.now())
      return redirect('AdminPanelAchievementView')
    
      
    data={
       "updater":request.user.username
       
    }
    return render(request,"AdminPanelAchievement.html",data)

@login_required(login_url='/Admin/')
def AdminPanelAchievementEdit(request,pk):
    form=Achievement.objects.get(id=pk)
    frm=form
    if(request.method=='POST'):
         experience_year=request.POST.get('experience_year')
         teacher_no=request.POST.get('teacher_no')
         bright_students=request.POST.get('bright_students')
         glorious_alumini=request.POST.get('glorious_alumini')
         Achievement.objects.filter(id=id).update(
            id=pk,
            year_of_experiences=experience_year,
            teacher_no=teacher_no,
            bright_students=bright_students,
            glorious_alumini=glorious_alumini,
            uploadby=CostumUser.objects.get(username=request.user.username),
            updateDate=timezone.now()

         )
         messages.success(request,"Successfully Edit")
         return redirect('AdminPanelAchievementView')
    data={
       "form":frm,
       "updater":request.user.username
    }
    return render(request,"AdminPanelAchievement.html",data)

@login_required(login_url='/Admin/')
def deleteachievement(request,pk):
   Achievement.objects.filter(id=pk).update(status="inactive")
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelAchievementView')


# introduction
@login_required(login_url='/Admin/')
def AdminPanelIntroductionView(request):
      Intro=Introduction.objects.all().filter(status='active').order_by('updateDate')[:1]
      data={
      'Intro':Intro,
      "updater":request.user.username,
      'category':request.user.category,

        }
      return render(request,"AdminPanelIntroductionView.html",data)

@login_required(login_url='/Admin/')
def AdminPanelIntroductionEdit(request,id):
   if(request.method=='POST'):
      form=IntroductionForm(request.POST)
      fp=request.POST.get('Introduction-para1')
      sp=request.POST.get('Introduction-para2')
      tp=request.POST.get('Introduction-para3')
      Introduction.objects.filter(id=id).update(
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=timezone.now()
         )
      return redirect('AdminPanelIntroductionView')
   form=Introduction.objects.get(id=id)
   data={
      "form":form,
      "updater":request.user.username
   }
   return render(request,'AdminPanelIntroduction.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelIntroductionAdd(request):
   form_id=Introduction.objects.filter(status='active')
   if(request.method=='POST'):
      form=IntroductionForm(request.POST)
      fp=request.POST.get('Introduction-para1')
      sp=request.POST.get('Introduction-para2')
      tp=request.POST.get('Introduction-para3')
      Intro=Introduction(
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         uploadby=CostumUser.objects.get(username=request.user.username),
         )
      Intro.save()
      messages.success(request,"Add successfully")
      form_id=form_id.values_list('id',flat=True)
      for x in form_id:
       Introduction.objects.filter(id=x).update(status='inactive',lastDate=timezone.now()) 

      return redirect('AdminPanelIntroductionView')

   data={
      "updater":request.user.username
   }
   return render(request,'AdminPanelIntroduction.html',data) 


# admin panel about
@login_required(login_url='/Admin/')
def AdminPanelAboutView(request):
   vision=AboutVision.objects.all().filter(status='active').order_by('updateDate')[:1]
   principle=AboutPrinciple.objects.all().filter(status='active').order_by('updateDate')[:1]
   history=AboutHistory.objects.all().filter(status='active').order_by('updateDate')[:1]
   data={
      'vision':vision,
      'principle':principle,
      'history':history,
      'updater':request.user.username,
      'category':request.user.category,
   
   }

   return render (request,'AdminPanelAboutView.html',data)


@login_required(login_url='/Admin/')
def AdminPanelAboutVision(request,vision_id):
   if request.method=='POST':
      fp=request.POST.get('vision-mission-para1')
      sp=request.POST.get('vision-mission-para2')
      tp=request.POST.get('vision-mission-para3')
      fop=request.POST.get('vision-mission-para4')
      AboutVision.objects.filter(id=vision_id).update(
         auto_increment_id=int(vision_id),
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=timezone.now()  )
      messages.success(request,'Successfully Edit')
      return redirect('AdminPanelAboutView')
   form=AboutVision.objects.get(auto_increment_id=vision_id)
   data={
   'updater':request.user.username,
    "form":form
    }
   
   return render(request,'AdminPanelAboutVision.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelAboutVisionAdd(request):
   form_id=AboutVision.objects.filter(status='active')
   if request.method=='POST':
      fp=request.POST.get('vision-mission-para1')
      sp=request.POST.get('vision-mission-para2')
      tp=request.POST.get('vision-mission-para3')
      fop=request.POST.get('vision-mission-para4')
      about=AboutVision(
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username), )
      about.save()
      messages.success(request,'Add successfully')
      
      form_id=form_id.values_list('id',flat=True)
      for x in form_id:
          AboutVision.objects.filter(id=x).update(status='inactive',lastDate=timezone.now())
      return redirect('AdminPanelAboutView')
   
   data={
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutVision.html',data) 


@login_required(login_url='/Admin/')
def AdminPanelAboutPrinciple(request,p_id):
   about=AboutPrinciple(auto_increment_id=p_id)
   postimg=about.img
   if(request.method=='POST'):
      
      if len(request.FILES) !=0:
         if len(str(about.img))>0:
            os.remove(about.img.path)
         img=request.FILES['principle-img']
         if type(img)==None:
            about.img=postimg
         else:
            about.img=img
         about.title=request.POST.get('principle-name')
         about.principleintro=request.POST.get('Short-Desc')
         about.firstpara=request.POST.get('principle-para1')
         about.secondpara=request.POST.get('principle-para2')
         about.thirdpara=request.POST.get('principle-para3')
         about.fourthpara=request.POST.get('principle-para4')
         about.uploadby=CostumUser.objects.get(username=request.user.username)
         about.updateDate=timezone.now()
         about.save()
         messages.success(request,'Successfully Update')
         return redirect('AdminPanelAboutView')
   form=AboutPrinciple.objects.get(auto_increment_id=p_id)
   data={
      'updater':request.user.username,
      "form":form
      }
   return render(request,'AdminPanelAboutPrinciple.html',data)

@login_required(login_url='/Admin/')
def AdminPanelAboutPrincipleAdd(request):
   about=AboutPrincipleForm(request.POST,request.FILES)
   form_id=Achievement.objects.filter(status='active')
   if(request.method=='POST'):
         about=AboutPrinciple()
         about.img=request.FILES['principle-img']
         about.title=request.POST.get('principle-name')
         about.principleintro=request.POST.get('Short-Desc')
         about.firstpara=request.POST.get('principle-para1')
         about.secondpara=request.POST.get('principle-para2')
         about.thirdpara=request.POST.get('principle-para3')
         about.fourthpara=request.POST.get('principle-para4')
         about.uploadby=CostumUser.objects.get(username=request.user.username)
         about.save()
         messages.success(request,'Successfully Update')
         form_id=form_id.values_list('id',flat=True)
         for x in form_id:
            Achievement.objects.filter(id=x).update(status='inactive',lastDate=timezone.now())
         return redirect('AdminPanelAboutView')
   data={
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutPrinciple.html',data)


@login_required(login_url='/Admin/')
def AdminPanelAboutHistory(request,history_id):
   if(request.method=='POST'):
      form=AboutHistoryForm(request.POST)
      fp=request.POST.get('History-para1')
      sp=request.POST.get('History-para2')
      tp=request.POST.get('History-para3')
      fop=request.POST.get('History-para4')
      AboutHistory.objects.filter(id=history_id).update(
         auto_increment_id=history_id,
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=timezone.now()
         )
      messages.success(request,'Successfully Edit')
      return redirect('AdminPanelAboutView')
   form=AboutHistory.objects.get(auto_increment_id=history_id)
   data={
      "form":form,
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutHistory.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelAboutHistoryAdd(request):
   form_id=AboutHistory.objects.filter(status='active')
   if(request.method=='POST'):
      form=AboutHistoryForm(request.POST)
      fp=request.POST.get('History-para1')
      sp=request.POST.get('History-para2')
      tp=request.POST.get('History-para3')
      fop=request.POST.get('History-para4')
      about=AboutHistory(
         firstpara=fp,
         secondpara=sp,
         thirdpara=tp,
         fourthpara=fop,
         uploadby=CostumUser.objects.get(username=request.user.username),
         )
      about.save()
      messages.success(request,'Add successfully ')
      form_id=form_id.values_list('id',flat=True)
      for x in form_id:
         AboutHistory.objects.filter(id=x).update(status='inactive',lastDate=timezone.now())
      return redirect('AdminPanelAboutView')
   data={
      'updater':request.user.username
   }
   return render(request,'AdminPanelAboutHistory.html',data) 
# admin panel admisiion
# @login_required(login_url='/Admin/')
# def AdminPanelAdmission(request):
#    return render(request,'AdminPanelAdmission.html',{'updater':request.user.username}) 



# admin panel notice
@login_required(login_url='/Admin/')
def AdminPanelNoticeAdd(request):
   if(request.method=='POST'):
      form=NoticeForm(request.POST,request.FILES)
      title=request.POST.get('notice_files_title')
      desc=request.POST.get('notice_files_description')
      img=request.FILES.get('notice_img')
      title2=request.POST.get('notice_file_title1')
      file2=request.FILES.get('notice_file1')
      title3=request.POST.get('notice_file_title2')
      file3=request.FILES.get('notice_file2')
      form=Notice(
          title=title,
          description=desc,
          file1=img,
          title2=title2,
          file2=file2,
          title3=title3,
          file3=file3,
          uploadby=CostumUser.objects.get(username=request.user.username),
       )
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelNoticeView')
   data={'updater':request.user.username}
   return render(request,'AdminPanelNotice.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelNoticeView(request):
   form=Notice.objects.all().filter(status='active').order_by('updateDate')
   data={
      'updater':request.user.username,
      "form":form,
      'category':request.user.category,

      }
   return render(request,'AdminPanelNoticeView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelNoticeEdit(request,pk):
   form=Notice.objects.get(id=pk)
   frm=form
   if(request.method=='POST'):
      form=NoticeForm(request.POST,request.FILES)
      Notice.objects.filter(id=pk).update(
      title=request.POST.get('notice_files_title'),
      description=request.POST.get('notice_files_description'),
      file1=request.FILES.get('notice_img'),
      title2=request.POST.get('notice_file_title1'),
      file2=request.FILES.get('notice_file1'),
      title3=request.POST.get('notice_file_title2'),
      file3=request.FILES.get('notice_file2'),
      uploadby=CostumUser.objects.get(username=request.user.username),
      updateDate=timezone.now())
      return redirect("AdminPanelNoticeView")

   data={
      'updater':request.user.username,
         "form":frm
         }
   return render(request,'AdminPanelNotice.html',data) 

@login_required(login_url='/Admin/')
def deletenotice(request,pk):
   Notice.objects.filter(id=pk).update(status='inactive')
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelNoticeView')




#  adminpanel samachar 
@login_required(login_url='/Admin/')
def AdminPanelNewsAdd(request):
   if(request.method=='POST'):
      form=NewsForm(request.POST)
      title=request.POST.get('samachar_title')
      link=request.POST.get('samachar_url')
      form=News(
          title=title,
          link=link,
          uploadby=CostumUser.objects.get(username=request.user.username),
       )
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelNewsView')
   data={
      'updater':request.user.username
      }
   return render(request,'AdminPanelNews.html',data)

@login_required(login_url='/Admin/')
def AdminPanelNewsView(request):
   form=News.objects.all().filter(status='active').order_by('updateDate')
   data={
      'category':request.user.category,
      'updater':request.user.username,"form":form,}
   return render(request,'AdminPanelNewsView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelNewsEdit(request,pk):
    form=News.objects.get(id=pk)
    frm=form
    if(request.method=='POST'):
         form.id=pk
         form.title=request.POST.get('samachar_title')
         form.link=request.POST.get('samachar_url')
         form.uploadby=CostumUser.objects.get(username=request.user.username),
      
         form.updateDate=timezone.now()
         form.save()
         return redirect('AdminPanelNewsView')
    data={
       'updater':request.user.username,
       "form":frm
       }
    return render(request,'AdminPanelNews.html',data) 

@login_required(login_url='/Admin/')
def deletenews(request,pk):
   News.objects.filter(id=pk).update(status='inactive')
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelNewsView')
  

# admin panel gallery
@login_required(login_url='/Admin/')
def AdminPanelGalleryView(request):
   form= Gallery.objects.all().filter(status='active').order_by('updateDate')
   data={
      'category':request.user.category,
      'updater':request.user.username,"form":form
      }
   return render(request,'AdminPanelGalleryView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelGalleryAdd(request):
    form=GalleryForm(request.POST,request.FILES)
    if(request.method =='POST'):
      form=Gallery()
      title=request.POST.get('gallery_img_title')
      img=request.FILES.get('gallery_img')
      
      form.title=title
      form.img=img
      form.uploadby=CostumUser.objects.get(username=request.user.username)
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelGalleryView')
    

    data={
       'updater':request.user.username
       }
    return render(request,'AdminPanelGallery.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelGalleryEdit(request,pk):
   form=Gallery.objects.get(id=pk)
   frm=form
   if(request.method=='POST'):
      if len(request.FILES) !=0:
         if len(str(form.img)) >0:
            os.remove(form.img.path)
         form.id=pk
         form.title=request.POST.get('gallery_img_title')
         form.img=request.FILES.get('gallery_img')
         form.uploadby=CostumUser.objects.get(username=request.user.username),
         form.updateDate=timezone.now()
         form.save()
         return redirect('AdminPanelGalleryView')
   
   data={
      'updater':request.user.username,
         "form":frm
         }
   return render(request,'AdminPanelGallery.html',data) 

@login_required(login_url='/Admin/')
def deletegallery(request,pk):
   form=Gallery.objects.get(id=pk)
   form.delete()
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelGalleryView')



# admin panel more
@login_required(login_url='/Admin/')
def AdminPanelMoreAdd(request):
   if(request.method=='POST'):
      form=MoreForm(request.POST,request.FILES)
      title=request.POST.get('file_title')
      file=request.FILES.get('filename')
      form=MoreDoc(
          title=title,
          file=file,
          uploadby=CostumUser.objects.get(username=request.user.username),
       )
      form.save()
      messages.info(request,"Successfully vayo")
      return redirect('AdminPanelMoreView')
   data={
      'updater':request.user.username
      }
   return render(request,'AdminPanelMore.html',data)

@login_required(login_url='/Admin/')
def AdminPanelMoreView(request):
   form=MoreDoc.objects.all().filter(status='active').order_by('updateDate')
      
   data={
      'category':request.user.category,
      'updater':request.user.username,
      "form":form}
   return render(request,'AdminPanelMoreView.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelMoreEdit(request,pk):
    form=MoreDoc.objects.get(id=pk)
    frm=form
    postfile=form.file
    if(request.method=='POST'):
      if len(request.FILES) !=0:
         if len(str(form.img)) >0:
            os.remove(form.img.path)
         form.id=pk
         form.title=request.POST.get('file_title')

         file=request.FILES.get('filename')
         if type(file)==None:
            form.file=postfile
         else:
            form.file=file
         form.uploadby=CostumUser.objects.get(username=request.user.username),
      
         form.updateDate=timezone.now()
         form.save()
         return redirect('AdminPanelMoreView')
    data={
       'updater':request.user.username,
       "form":frm
       }
    return render(request,'AdminPanelMore.html',data) 

@login_required(login_url='/Admin/')
def deletemore(request,pk):
   MoreDoc.objects.filter(id=pk).update(status='inactive')
   messages.info(request,"Delete successfully")
   return redirect('AdminPanelMoreView')



# admin panel contact
@login_required(login_url='/Admin/')
def AdminPanelContactLinkView(request):
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   social=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   data={
      'contact':contact,
      'social':social,
      'updater':request.user.username,
      'category':request.user.category,

      }
   return render (request,'AdminPanelContactLinkView.html',data)


@login_required(login_url='/Admin/')
def AdminPanelContactAdd(request):
   if request.method=='POST':
      contact=Contact(
         location=request.POST.get('location_link'),
         gmail_api=request.POST.get('gmail_api'),
         gmail=request.POST.get('gmail_link'),
         phn_no=request.POST.get('phn_no'),uploadby=CostumUser.objects.get(username=request.user.username),
           ),
         
      contact.save()
      return redirect('AdminPanelContactLinkView')
   data={
      'updater':request.user.username}
   return render(request,'AdminPanelContact.html',data) 

@login_required(login_url='/Admin/')
def AdminPanelContactEdit(request,pk):
   if request.method=='POST':
      contact=Contact(
         id=int(pk),
         location=request.POST.get('location_link'),
         gmail_api=request.POST.get('gmail_link'),
         gmail=request.POST.get('gmail_api'),
         phn_no=request.POST.get('phn_no'),
         uploadby=CostumUser.objects.get(username=request.user.username),
         updateDate=timezone.now()  )
      contact.save()
      return redirect('AdminPanelContactLinkView')
   form=Contact.objects.get(id=pk)
   data={
      'updater':request.user.username,
      "form":form
      }
   return render(request,'AdminPanelContact.html',data)


@login_required(login_url='/Admin/')
def AdminPanelSocialAdd(request):
   if(request.method=='POST'):
      social=Social()
      social.facebook=request.POST.get('facebook_link')
      social.twitter=request.POST.get('twitter_link')
      social.linkedin=request.POST.get('linkedin_link')
      social.uploadby=CostumUser.objects.get(username=request.user.username),
      social.save()
      return redirect('AdminPanelContactLinkView')
   data={
      'updater':request.user.username
         }
   return render(request,'AdminPanelSocial.html',data)

@login_required(login_url='/Admin/')
def AdminPanelSocialEdit(request,pk):
   if(request.method=='POST'):
      social=Social()
      social.id=pk
      social.facebook=request.POST.get('facebook_link')
      social.twitter=request.POST.get('twitter_link')
      social.linkedin=request.POST.get('linkedin_link')
      social.uploadby=CostumUser.objects.get(username=request.user.username),
      social.updateDate=timezone.now()
      social.save()
      return redirect('AdminPanelContactLinkView')
   
   form=Social.objects.get(id=pk)
   
   data={
      'updater':request.user.username,
      "form":form,
      }
   return render(request,'AdminPanelSocial.html',data)


# contact form view
@login_required(login_url='/Admin/')
def AdminPanelContactsView(request):
   form=ViewerContacts.objects.all().filter(status='active')
   return render (request,'AdminPanelContactsView.html',{'updater':request.user.username,"form":form})

# admin profile
@login_required(login_url='/Admin/')
def AdminProfile(request):
   form=""
   try:
      form=User_profile.objects.get(username=request.user.username)
      
   except Exception:
      messages.info(request,'sorry you doesnot have profile')
      return redirect('AdminProfileAdd')
   data={
      "updater":request.user.username,
      "category":request.user.category,
      'form':form,
   }
   return render(request,'AdminProfile.html',data)


@login_required(login_url='/Admin/')
def AdminProfileEdit(request,pk):
   return render(request,'AdminProfileEdit.html')


@login_required(login_url='/Admin/')
def AdminProfileAdd(request):
   form=User_profileForm(request.POST,request.FILES)
   if(request.method == 'POST'):
            form.username=request.user.username
            form.userid=CostumUser.objects.get(username=request.user.username).userid
            form=User_profile()
            form.first_name=request.POST.get('first_name')
            form.middle_name=request.POST.get('middle_name')
            form.last_name=request.POST.get('last_name')
            form.post=request.POST.get('admin_post')
            form.img=request.FILES.get('gallery_img')
            form.phn_no=request.POST.get('phn_no')
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('AdminProfile') 
   
   arr=['Administrator','Teacher','Principle']
   data={
      "updater":request.user.username,
      "category":request.user.category,
      'form':form,
      'arr':arr,
   }
   return render(request,'AdminProfileEdit.html',data)


@login_required(login_url='/Admin/')
def AdminNewModeratorAdd(request):
  
   return render(request,'AdminNewModerator.html')



@login_required(login_url='/Admin/')
def AdminProfilechangePassword(request):
   return render(request,'AdminProfilechangePassword.html')



