from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from App.models import UserModel


def index(request):
    return render(request,'index.html')

def upload_file(request):

    if request.method=='GET':
        return render(request,'upload.html')
    elif request.method=='POST':
        icon = request.FILES.get('icon')

        print(type(icon))

        with open('/root/GP1/ModelToSQL/static/img/cet6.jpg','wb') as file1:
            for i in icon.chunks():
                file1.write(i)
                file1.flush()

        return HttpResponse('upload success!')


def image_field(request):
    if request.method=='GET':
        return render(request,'image_field.html')
    elif request.method=='POST':
        username = request.POST.get('username')
        icon = request.FILES.get('icon')
        user = UserModel()
        user.u_name = username
        user.u_icon = icon

        user.save()

        return HttpResponse("NO%d upload success!" % user.id)


def mine(request):

    username = request.GET.get('username')

    user = UserModel.objects.get(u_name=username)

    data = {
        "username":username,
        "icon_url":"/static/upload/"+user.u_icon.url,
    }

    return render(request,'mine.html',context=data)