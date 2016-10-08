from django.test import TestCase    # 是unittest.TestCase 的增强版
from django.core.urlresolvers import resolve  # resolve[做出决定]
from lists.views import home_page   # 必须在 views.py 中创建 home_page()
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """单元测试:是否能把 '/' 解析到 view 中的 home_page()函数"""
        found = resolve('/')  # 解析 '/',会分配 func
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # 因为网络传输的内容是 原始字符
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
