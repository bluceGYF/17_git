from django.shortcuts import render


# help主页
def help(request):

    return render(request, 'help/help.html', locals())
