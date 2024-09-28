from django.shortcuts import render

def common(request):
    return render(request, template_name='common/home-page.html')





