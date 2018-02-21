from django.shortcuts import render, render_to_response
from .models import OseroPanel, Book, AllPanel
from .forms import Players
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
import pdb

@csrf_protect
def start(request):
    players = Players()
    if 'style' in request.POST:
            datas = '00000000000000000000000000021000000120000000000000000000000000003'
            Book.objects.all().delete()
            AllPanel.objects.all().delete()
            Book.objects.get_or_create(panel=54)
            AllPanel.objects.get_or_create(allpanel=datas)
            return HttpResponseRedirect('/osero/play/')
    c = {'players':players}
    return render(request, 'app/start.html',c)


@csrf_protect
def index(request):
    places = []
    if request.method == "POST":
        if "point" in request.POST:
            objs = AllPanel.objects.all()[0].allpanel
            for obj in objs:
                places.append(int(obj))
            print(places)
            b_places = places
            points = request.POST.get('point')
            switch = points.split(",")
            point_x = int(switch[0])
            point_y = int(switch[1])
            point = point_x * 8 + point_y
            if places[point] == 0:
                if places[64] == 3:
                    places[64] = 4
                    places[point] = 1
                    reverse_point=1
                elif places[64] == 4:
                    places[64] = 3
                    places[point] = 2
                    reverse_point=2
                text_str = ""
                places = ReversePanel(places, point_x, point_y,reverse_point,b_places)
                for place in places:
                    text_str += str(place)
                AllPanel.objects.all().delete()
                AllPanel.objects.get_or_create(allpanel=text_str)
        else:
            return HttpResponseRedirect('/osero/start/')
    else:
        print("begin")
        datas = AllPanel.objects.all()[0].allpanel
        for data in datas:
            places.append(int(data))
    packages = Set_Panel(places)
    which = ""
    if places[64] == 0:
        which = "黒番"
    elif places[64] == 1:
        which = "白番"
    c = {'packages': packages, 'which':which}
    print("index")
    return render(request, 'app/index.html', c)



def Set_Panel(places):
    packages = []
    pic_green = OseroPanel.objects.get(file="green.png")
    pic_white = OseroPanel.objects.get(file="white.png")
    pic_black = OseroPanel.objects.get(file="black.png")

    for i in range(8):
        items = []
        for j in range(8):
            arr = places[i*8+j]
            if arr == 1:
                items.append({'item': [pic_black.file, i, j, places[64]]})
            elif arr == 2:
                items.append({'item': [pic_white.file, i, j, places[64]]})
            else:
                items.append({'item': [pic_green.file, i, j, places[64]]})
        packages.append({'items': items})
    return packages

def ReversePanel(places, x, y,reverse,b_places):
    x_line = []
    y_line = []
    left_line = []
    right_line = []
    left_s = x-y
    right_s = y+x
    for i in range(8):
        j = i*8
        x_line.append(places[y+j])
        y_line.append(places[x+j])
        if left_s + i >= 0 and left_s+j+i <64:
            left_line.append(places[left_s+j+i])
        if right_s+j+i <64:
            print(places[right_s+j+i])
            right_line.append(places[right_s+8+i*7])
    print(x_line,y_line,left_line,right_line,x,y)
    blocks = []
    for i in range(8):
        for j in range(8):
            blocks.append([i,j,places[i*8+j]])
    re_places = []
    for block in blocks:
        if block[0] == x and block[2] != 0:
            block[2] = reverse
        if block[1] == y and block[2] != 0:
            block[2] = reverse
        re_places.append(block[2])
    re_places.append(places[64])
    return re_places
