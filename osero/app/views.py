from django.shortcuts import render
from django.http import HttpResponse
from .models import OseroPanel
import pdb
# Create your views here.

def index(request):
    if request.POST:
        print(request.POST)
    c = {}
    place =[]
    datas = '0000000000000000000000000002100000012000000000000000000000000000'
    for data in datas:
        place.append(int(data))
    packages = []
    pic = OseroPanel.objects.get(file="green.png")
    pic_white = OseroPanel.objects.get(file="white.png")
    pic_black = OseroPanel.objects.get(file="black.png")
    for  i in range(8):
        items=[]
        for j in range(8):
            arr = place[i*8+j]
            if arr == 1:
                items.append({ 'item' : [pic_black.file, i, j] })
            elif arr == 2:
                items.append({ 'item' : [pic_white.file,i ,j] })
            else:
                items.append({ 'item' : [pic.file, i, j] })
        packages.append({ 'items' : items })
    c = {'packages':packages,'items':items}
    return render(request, 'app/index.html',c)
