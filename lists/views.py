from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')  # 1:请求对象 2:渲染的模板
    # Django会在所有的应用目录下搜索 templates目录,根据模板内容
    # 构建一个 HttpResponse 对象
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()  # items 传递给 render() 会自动替换 HTML 中的 Python变量  items
    return render(request, 'list.html', {'items': items, })


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
