from django.db import models



class kind(models.Model):
    name = models.CharField(max_length=200,help_text="enter a furniture kind: ")

    def __str__(self):
        return self.name


class furniture(models.Model):
    title = models.CharField(max_length=200)
    kind = models.ManyToManyField(kind,help_text="select a kind for this furniture: ")
    brand = models.ForeignKey('Brand',on_delete=models.SET_NULL, null=True)
    pic = models.ImageField(blank = True,null=True,upload_to='furniture/%Y%m%d')
    slug = models.SlugField(max_length = 100,unique = True,null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('furniture-details',args=[self.id,self.slug])
    class Meta:
          ordering=('title',)
          index_together=(('id','slug'),)

 

class Brand(models.Model):
    name = models.CharField(max_length=200,help_text='enter a furniture brand: ')
    
    def __str__(self):
        return self.name

class furniture_detail_photos(models.Model):
    furniture = models.OneToOneField('furniture',on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/%Y%m%d',null=True,blank=True)
    def __str__(self):
        return self.furniture
# Create your models here.
