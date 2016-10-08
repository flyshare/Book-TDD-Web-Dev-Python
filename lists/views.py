from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html') # 1:请求对象 2:渲染的模板 
                                        # Django会在所有的应用目录下搜索 templates目录,根据模板内容
                                        # 构建一个 HttpResponse 对象
