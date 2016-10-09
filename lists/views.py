from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')  # 1:请求对象 2:渲染的模板
    # Django会在所有的应用目录下搜索 templates目录,根据模板内容
    # 构建一个 HttpResponse 对象
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        if new_item_text:
            # 创建Item()对象的简化方式,而无需调用 .save()
            Item.objects.create(text=new_item_text)
        return redirect('/')

    items = Item.objects.all()  # items 传递给 render() 会自动替换 HTML 中的 Python变量  items
    return render(request, 'home.html', {'items': items, })
