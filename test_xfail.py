"""
标记为xfail的方法，在执行失败时会被略过，不算作失败记录
"""
import pytest


class TestXFail:

    @pytest.mark.xfail(reason='该方法尚未完成')
    def test_xfail1(self):
        print('-----start-----')
        # 也可以通过这种方式标记，不推荐
        # pytest.xfail(reason='该方法尚未完成')
        print('test_one方法执行')
        assert 1 == 2

    @pytest.mark.xfail(raises=ZeroDivisionError)
    def test_xfail2(self):
        # 指定抛出某个异常之后忽略该用例
        assert 1 / 0

    @pytest.mark.xfail(raises=ValueError)
    def test_xfail3(self):
        assert 1 / 0

    def test_one(self):
        print('test_two方法执行')
        assert 1 == 2

    def test_two(self):
        print('test_three方法执行')
        assert 1 == 1
