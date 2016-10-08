from django.test import TestCase    # 是unittest.TestCase 的增强版
from django.core.urlresolvers import resolve  # resolve[做出决定]
from lists.views import home_page   # 必须在 views.py 中创建 home_page()
from django.http import HttpRequest
from django.template.loader import render_to_string


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

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        # print(response.content.decode())
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html', {'new_item_text': 'A new list item'})
        print(response.content.decode())
        self.assertEqual(response.content.decode(), expected_html)
