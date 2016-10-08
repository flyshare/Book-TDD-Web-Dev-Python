from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')  # 1:请求对象 2:渲染的模板
    # Django会在所有的应用目录下搜索 templates目录,根据模板内容
    # 构建一个 HttpResponse 对象
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', ''), })
