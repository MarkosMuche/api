from django.shortcuts import render


def aboutme(requests):

    return render(request=requests, template_name='about_me.html')
