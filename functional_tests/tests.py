from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    """"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)  # 这是隐式等待,如果逻辑复杂,需要使用更复杂的 显示等待

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """"""
        # 伊迪丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get(self.live_server_url)
        # 她注意到网页的标题和头部都包含 "To-Do" 这个词
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')

        # 她在一个文本框中输入了 "Buy peacock feathers" (购买孔雀羽毛)
        # 伊迪丝的爱好是使用假蝇做饵钓鱼
        inputbox.send_keys('Buy peacock feathers')
        #
        # 她按回车键后,页面更新了
        # 待办事项表格中显示了 "1. Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        # table = self.browser.find_element_by_id(
        # 'id_list_table')    # 如没有找到元素就抛出异常
        # rows = table.find_elements_by_tag_name('tr')    # 没有找到就返回一个空 list
        # print('table.text: ', table.text) # 它的值是由 Keys.ENTER 提交而来
        # time.sleep(10)
        # self.assertTrue(
        #     any(row.text == '1. Buy peacock feathers' for row in rows), \
        #     "New to-do item did not appear in table -- its text was:\n%s" % (table.text,))
        # self.assertIn('1. Buy peacock feathers', [row.text for row in rows])

        # 页面中有显示了一个文本框,可以输入其他的待办事项
        # 她输入了 "Use peacock feathers to make a fly" (使用孔雀羽毛做假蝇)
        # 伊迪丝做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新,她的清单中显示了这两个待办事项
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2. Use peacock feathers to make a fly')
        # 伊迪丝想知道这个网站是否能记住她的清单
        # 她看到网站为她生成了一个唯一的 URL
        # 而且页面中有一些文字解说这个功能
        self.fail('Finish the test!')
        # 她访问了这个 URL,发现她的待办事项列表还在