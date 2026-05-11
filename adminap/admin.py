from django.contrib import admin

# Register your models here.
from adminap.models import *
# swiper
admin.site.register(HomeSwiper)

# about
admin.site.register(AboutVision)
admin.site.register(AboutPrinciple)
admin.site.register(AboutHistory)

# notice
admin.site.register(Notice)

# gallery
admin.site.register(Gallery)

# more / document
admin.site.register(MoreDoc)

# news
admin.site.register(News)

# contact
admin.site.register(Contact)

# social
admin.site.register(Social)
# Achievement
admin.site.register(Achievement)
# introduction
admin.site.register(Introduction)
# admin.site.register(Moderator)
# admin.site.register(Admin)


admin.site.register(CostumUser)

admin.site.register(ProvinceInformation)
admin.site.register(DistrictInformation)
admin.site.register(MunicipalityInformation)