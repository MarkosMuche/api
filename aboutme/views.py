from django.shortcuts import render


def index_view(request):

    return render(request, 'index.html')


def aboutme(requests):

    return render(request=requests, template_name='about_me.html')
