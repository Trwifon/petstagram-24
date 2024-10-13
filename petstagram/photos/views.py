from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)

def photo_details(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request,'photos/photo-details-page.html', context)


def photo_edit(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)

    context = {
        'photo': photo,
        'form': form,
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete(request, pk: int):
    return render(request, template_name='photos/photo-delete-page.html')