from django.urls import path

from . import views
from django.urls import path

from . import views

urlpatterns = [
    # adminpanels
    # admin panel dashboard
     path('AdminPanelHome/', views.AdminPanelHome ,name='AdminPanelHome'),
    
    # swiprer
     path('AdminPanelHomeSwiperView/', views.AdminPanelHomeSwiperView ,name='AdminPanelHomeSwiperView'),
     path('AdminPanelHomeSwiperAdd/', views.AdminPanelHomeSwiperAdd ,name='AdminPanelHomeSwiperAdd'),
     path('AdminPanelHomeSwiperEdit/<int:id>', views.AdminPanelHomeSwiperEdit ,name='AdminPanelHomeSwiperEdit'),
      path('deleteswiper/<int:pk>', views.deleteswiper ,name='deleteswiper'),

    # school achievement
    path('AdminPanelAchievementView/', views.AdminPanelAchievementView ,name='AdminPanelAchievementView'),
    path('AdminPanelAchievementAdd/', views.AdminPanelAchievementAdd ,name='AdminPanelAchievementAdd'),
    path('AdminPanelAchievementEdit/<int:pk>', views.AdminPanelAchievementEdit ,name='AdminPanelAchievementEdit'),
     path('deleteachievement/<int:pk>', views.deleteachievement ,name='deleteachievement'),

# admin about pages
    path('AdminPanelAboutView/', views.AdminPanelAboutView ,
    name='AdminPanelAboutView'),

    path('AdminPanelAboutVision/<int:vision_id>', views.AdminPanelAboutVision ,
    name='AdminPanelAboutVision'),
    path('AdminPanelAboutVisionAdd/', views.AdminPanelAboutVisionAdd ,
    name='AdminPanelAboutVisionAdd'),

     path('AdminPanelAboutPrinciple/<int:p_id>', views.AdminPanelAboutPrinciple ,name='AdminPanelAboutPrinciple'),
     path('AdminPanelAboutPrincipleAdd/', views.AdminPanelAboutPrincipleAdd ,name='AdminPanelAboutPrincipleAdd'),

     path('AdminPanelAboutHistory/<int:history_id>', views.AdminPanelAboutHistory ,name='AdminPanelAboutHistory'),
     path('AdminPanelAboutHistoryAdd/', views.AdminPanelAboutHistoryAdd ,name='AdminPanelAboutHistoryAdd'),
     
     
     
    #  introduction
     path('AdminPanelIntroductionView/', views.AdminPanelIntroductionView ,name='AdminPanelIntroductionView'),
     path('AdminPanelIntroductionEdit/<int:id>', views.AdminPanelIntroductionEdit ,name='AdminPanelIntroductionEdit'),
     path('AdminPanelIntroductionAdd/', views.AdminPanelIntroductionAdd ,name='AdminPanelIntroductionAdd'),

    #  admin panel admission
    #  path('AdminPanelAdmission/', views.AdminPanelAdmission ,
    # name='AdminPanelAdmission'),

     # admin panel notice
    path('AdminPanelNoticeAdd/', views.AdminPanelNoticeAdd ,name='AdminPanelNoticeAdd'),
    path('AdminPanelNoticeView/', views.AdminPanelNoticeView ,name='AdminPanelNoticeView'),
    path('deletenotice/<int:pk>', views.deletenotice ,name='deletenotice'),
    path('editnotice/<int:pk>', views.AdminPanelNoticeEdit ,name='editnotice'),




      # admin panel gallery 

    path('AdminPanelGalleryView/', views.AdminPanelGalleryView ,name='AdminPanelGalleryView'),
    path('AdminPanelGalleryAdd/', views.AdminPanelGalleryAdd ,name='AdminPanelGalleryAdd'),
    path('AdminPanelGalleryEdit/<int:pk>', views.AdminPanelGalleryEdit ,name='AdminPanelGalleryEdit'),
    path('deletegallery/<int:pk>', views.deletegallery ,name='deletegallery'),

    
    # admin panel more
    path('AdminPanelMoreAdd/', views.AdminPanelMoreAdd ,name='AdminPanelMoreAdd'), 
    path('AdminPanelMoreView/', views.AdminPanelMoreView ,name='AdminPanelMoreView'),
    path('AdminPanelMoreEdit/<int:pk>', views.AdminPanelMoreEdit ,name='AdminPanelMoreEdit'),
    path('deletemore/<int:pk>', views.deletemore,name='deletemore'),

    # adminpanel samachar
    path('AdminPanelNewsAdd/', views.AdminPanelNewsAdd ,name='AdminPanelNewsAdd'), 
    path('AdminPanelNewsView/', views.AdminPanelNewsView ,name='AdminPanelNewsView'),
    path('AdminPanelNewsEdit/<int:pk>', views.AdminPanelNewsEdit ,name='AdminPanelNewsEdit'),
    path('deletenews/<int:pk>', views.deletenews,name='deletenews'),
   

    # contact and links pages
    path('AdminPanelContactLinkView/', views.AdminPanelContactLinkView ,name='AdminPanelContactLinkView'),


    path('AdminPanelContactAdd/', views.AdminPanelContactAdd ,name='AdminPanelContactAdd'),
    path('AdminPanelContactEdit/<int:pk>', views.AdminPanelContactEdit ,name='AdminPanelContactEdit'),

    path('AdminPanelSocialAdd/', views.AdminPanelSocialAdd ,name='AdminPanelSocialAdd'),
    path('AdminPanelSocialEdit/<int:pk>', views.AdminPanelSocialEdit ,name='AdminPanelSocialEdit'),

   
# contats form
     path('AdminPanelContactsView/', views.AdminPanelContactsView ,name='AdminPanelContactsView'),

     path('AdminProfile/', views.AdminProfile ,name='AdminProfile'),
     path('AdminProfileEdit/<str:pk>', views.AdminProfileEdit ,name='AdminProfileEdit'),
     path('AdminProfileAdd/', views.AdminProfileAdd ,name='AdminProfileAdd'),
     path('AdminProfilechangePassword/', views.AdminProfilechangePassword ,name='AdminProfilechangePassword'),

     path('AdminNewModerator/', views.AdminNewModeratorAdd ,name='AdminNewModerator'),



]
