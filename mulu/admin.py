from django.contrib import admin
from mulu.models import kind,furniture,Brand,furniture_detail_photos
from django.utils.safestring import mark_safe


# Register your models here.

class furniture_list(admin.ModelAdmin):
	list_display = ('title','brand')
class photoinline(admin.StackedInline):
	model = furniture_detail_photos
	extra = 3

class picAdmin(admin.ModelAdmin):

	inlines = [photoinline]
	#def save_model(self,request,obj,form,change):
		#super(PostAdmin,self).save_model(request, obj, form, change)

		#for afile in request.FILES.getlist('photos_multiple'):
			#obj.images.create(file=afile)
	list_display = ['title','brand','pic']
    
    




admin.site.register([kind,Brand])
admin.site.register(furniture,picAdmin)
