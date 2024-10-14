from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from petstagram.accounts.views import profile_details
from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


def add_pet(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)
    context = {'form': form,}

    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form
    }

    return render(request, 'pets/pet-details-page.html', context)


def pet_edit(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()

            return  redirect('pet-details', username, pet_slug)

    context = {
        'form': form,
    }
    return render(request, template_name='pets/pet-edit-page.html', context=context)


def pet_delete(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', username, pk = 1)

    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-delete-page.html', context=context)


