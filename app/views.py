from django.shortcuts import redirect, render
from .models import Categories, Photo


def gallery(request):
    photos = Photo.objects.all()    

    categories = Categories.objects.all()
    context = {'categories':categories, 'photos': photos}
    return render(request, 'app/gallery.html',context)


def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'app/photo.html',{"photo":photo})


def addPhoto(request):
    categories = Categories.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Categories.objects.get(id = data['category'])
        elif data['category_new'] != '':
            category, created = Categories.objects.get_or_create(name= data['category_new'])
        else:
            category = None


        photo = Photo.objects.create(
        category = category,
        description = data['description'],
        image = image,
    )        
        return redirect('gallery')
    context = {"categories":categories}
    return render(request, 'app/add.html',context)


def viewCat(request,pk):
    category = Categories.objects.get(id= pk)
    photos = Photo.objects.filter(category__name = category)
    return render(request, 'app/category.html',{'category':category, 'photos': photos})