"""
pytest结合allure实现报告输出
"""
import allure
import pytest


@allure.feature('购物车')
class TestShoppingTrolley:

    @allure.story('加入购物车')
    def test_add_shopping_trolley(self):
        login('test_user', 'test_pwd')
        with allure.step('浏览商品'):
            allure.attach('笔记本', '商品1')
            allure.attach('手机', '商品2')
        with allure.step('点击商品'):
            pass
        with allure.step('校验结果'):
            allure.attach('添加购物车成功', '期望结果')
            allure.attach('添加购物车失败', '实际结果')
            assert 'success' == 'failed'

    @allure.story('修改购物车')
    def test_edit_shopping_trolley(self):
        pass

    @pytest.mark.skipif(reason='本次不执行')
    @allure.story('删除购物城中的商品')
    def test_delete_shopping_trolley(self):
        pass


@allure.step('用户登录')
def login(user, pwd):
    print(f'{user} {pwd}')
