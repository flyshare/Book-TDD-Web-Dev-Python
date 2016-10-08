from django.test import TestCase    # 是unittest.TestCase 的增强版
from django.core.urlresolvers import resolve  # resolve[做出决定]
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        """单元测试:是否能把 '/' 解析到 view 中的 home_page()函数"""
        found = resolve('/')  # 解析 '/',会分配 func
        self.assertEqual(found.func, home_page)
