from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20, blank= False, null= False)


    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank= True, null= True)
    image = models.ImageField(upload_to='images', null= False, blank= False)
    description = models.TextField()

    def __str__(self):
        return self.description