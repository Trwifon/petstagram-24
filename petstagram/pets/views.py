from django.shortcuts import render


def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def pet_details(request, username: str, pet_slug: str):
    return render(request, template_name='pets/pet-details-page.html')


def pet_edit(request):
    return render(request, template_name='pets/pet-edit-page.html')


def pet_delete(request):
    return render(request, template_name='pets/pet-delete-page.html')


