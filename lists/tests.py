from django.test import TestCase    # 是unittest.TestCase 的增强版
from django.core.urlresolvers import resolve  # resolve[做出决定]
from lists.views import home_page   # 必须在 views.py 中创建 home_page()
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item, List


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """单元测试:是否能把 '/' 解析到 view 中的 home_page()函数"""
        found = resolve('/')  # 解析 '/',会分配 func
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # 因为网络传输的内容是 原始字符
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))
        expected_html = render_to_string('home.html')
        # 因为 网络传输的内容是 utf8编码,而加载到内存的都是 Unicdoe 编码
        self.assertEqual(response.content.decode(), expected_html)


class ListAndItemModelsTest(TestCase):
    """"""

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):
    """"""

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_display_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

        response = self.client.get('/lists/the-only-list-in-the-world/')

        # Django 的assertContains() 知道如何处理响应以及响应内容中的字节
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 1')


class NewListTest(TestCase):
    """"""

    def test_home_page_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item', })
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new', data={'item_text': 'A new list item', })
        self.assertEqual(response.status_code, 302)  # 302 状态码,是否重定向
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
