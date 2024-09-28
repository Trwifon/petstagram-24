from django.shortcuts import render

def add_photos(request):
    return render(request, template_name='photos/photo-add-page.html')

def photo_details(request, pk: int):
    return render(request, template_name='photos/photo-details-page.html')

def photo_edit(request, pk: int):
    return render(request, template_name='photos/photo-edit-page.html')

