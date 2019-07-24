from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from mulu.models import kind
from mulu.models import furniture
from .forms import FurnitureDetails
# coding:utf-8

def kind_list(request):
    
    kinds= kind.objects.all()
    furnitures= furniture.objects.all()


    return render(request,'mulu/catalog.html',{'kinds':kinds,'furnitures':furnitures})

  
def furniture_list(request,fur_kind=None):
    kind = get_object_or_404(kind)
    furnitures = furniture.objects.filter(available=True)
    show = furnitures.filter(fur_kind=kind)
    return render(request, 'mulu/furniture.html',{'show':show,'kind':kind})

def upload_details(request,id=None):
	name = furniture.objects.get(id=id)
	form = FurnitureDetails(instance=name)
	def form_upload(request):
		if request.method =='POST':
			form = FurnitureDetails(request.POST,request.FILES)
			if form.is_valid():
				form.save()
				return redirect('')
		else:
			form= FurnitureDetails()

	return render(request,'upload.html',{'name':name,'form':form})



