from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import Photo


def common(request):
    all_photos = Photo.objects.all()

    content = {'all_photos': all_photos}

    return render(request, 'common/home-page.html', content)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_objects = Like.objects.filter(to_photo=photo.id).first()

    if liked_objects:
        liked_objects.delete()
    else:
        liked_objects = Like(to_photo=photo)
        liked_objects.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')




