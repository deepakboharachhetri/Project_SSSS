from django.shortcuts import render,redirect

from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from adminap.models import *
from adminap.models import AboutHistory
from schoolap.models import ViewerContacts
from schoolap.forms import ViewerContactsForm
from django.core.paginator import Paginator

User=get_user_model()


# Create your views here.
def index(request):
   form=HomeSwiper.objects.all().filter(status='active').filter(status='active').order_by('updateDate')
   vision=AboutVision.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:1]
   principle=AboutPrinciple.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:1]
   notice=Notice.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:5]
   news=News.objects.all().filter(status='active') .order_by('updateDate')[:5]
   links=Social.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:1]
   Intro=Introduction.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:1]
   scroller=Notice.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:8]
   achievement=Achievement.objects.all().filter(status='active').filter(status='active').order_by('updateDate')[:1]
   data={'form':form,
         'vision':vision,
         'principle':principle,
         'notice':notice,
         'news':news,
         'links':links,
         'contact':contact,
         'scroller':scroller,
         'intro':Intro,
         'achievement':achievement
         }
   return render(request,'index.html',data) 


def AboutHist(request):
   scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
   links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   history=AboutHistory.objects.all().filter(status='active').order_by('updateDate')[:1]
   data={'history':history,
         'contact':contact,
         'links':links,
         'scroller':scroller
         }
   return render(request,'AboutHistory.html',data) 


def AboutPrincipleMessage(request):
   scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
   links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   principle=AboutPrinciple.objects.all().filter(status='active').order_by('updateDate')[:1]
   data={'principle':principle,
         'contact':contact,
         'links':links,
         'scroller':scroller
         }
   return render(request,'AboutPrincipleMessage.html',data) 


def AboutVisionMission(request):
      scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
      links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
      contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
      vision=AboutVision.objects.all().filter(status='active').order_by('updateDate')[:1]
      data={'vision':vision,
            'contact':contact,
            'links':links,
            'scroller':scroller
            }
      return render(request,'AboutVisionMission.html',data) 






def contact(request):
   scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
   links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   if(request.method=='POST'):
      form=ViewerContactsForm(request.POST)
      viewer=ViewerContacts()
      viewer.fullname=request.POST.get('fullname')
      viewer.email=request.POST.get('email')
      viewer.subject=request.POST.get('subject')
      viewer.message=request.POST.get('message')
      viewer.save()
      messages.info(request,"Successfully send")
   data={
       'links':links,
       'contact':contact,
       'scroller':scroller}
   return render(request,'contact.html',data) 


def gallery(request):
   scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
   links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   gallery=Gallery.objects.all().filter(status='active').order_by('updateDate')
   data={'gallery':gallery,
         'contact':contact,
         'links':links,
         'scroller':scroller
         }
   return render(request,'gallery.html',data) 



def more(request):
   scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
   links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   more=MoreDoc.objects.all().filter(status='active').order_by('updateDate')
   data={'more':more,
         'contact':contact,
         'links':links,
         'scroller':scroller
         }
   return render(request,'more.html',data) 

def notices(request):
   scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
   links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   news=News.objects.all().filter(status='active').order_by('updateDate')
   notice=Notice.objects.all().filter(status='active').order_by('updateDate')
   paginator1=Paginator(notice,10)
   paginator2=Paginator(news,10)
   page_number=request.GET.get('page')
   page_no=request.GET.get('page_no')
   noticefinal=paginator1.get_page(page_no)
   newsfinal=paginator2.get_page(page_number)

   data={
       'links':links,
       'contact':contact,
       'notice':noticefinal,
       'news':newsfinal,
       'scroller':scroller
       }
   return render(request,'notices.html',data) 

def Notice_Open(request,pk):
   scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
   links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
   contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]
   form=Notice.objects.get(id=pk)
   data={'form':form,
         'links':links,
         'contact':contact,
          'scroller':scroller
         }
   return render(request,'Notices_Open.html',data) 





# admin check

# admin username

def Admin(request):
    scroller=Notice.objects.all().filter(status='active').order_by('updateDate')[:8]
    links=Social.objects.all().filter(status='active').order_by('updateDate')[:1]
    contact=Contact.objects.all().filter(status='active').order_by('updateDate')[:1]

    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            check_status=CostumUser.objects.get(username=username).status
            if check_status==True:
               login(request,user)
               messages.success(request,("successfully login"))
               return redirect('AdminPanelHome')
            else:
               messages.error(request,("Sorry you are not available..."))
               return render(request,'Admin.html')


                
                
        else:
            messages.error(request,("Invalid User"))
            return render(request,'Admin.html')
    data={'links':links,
               'contact':contact,
               'scroller':scroller
              }
    return render (request,'Admin.html',data)
    
def logout_user(request):
    messages.success(request,("successfully logout"))
    logout(request)
    return redirect('/')



