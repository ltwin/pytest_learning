"""
raise，指定方法会抛出的异常之后，在运行测试用例时，该方法抛出的该异常将被捕获
"""
import pytest


def func():
    return 1 / 0


def func1():
    raise ValueError('Exception 123 raised')


def test_func():
    # 捕获对应类型的异常
    with pytest.raises(ZeroDivisionError) as exec_info:
        func()
    assert 'division by zero' in str(exec_info.value)


def test_match():
    # 匹配异常信息中的字符串，进行捕获
    # 请注意这里的match实际使用的是re.search，因此使用'123'也可以匹配到
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        func1()


def test_direct_run():
    # 也可以直接在raises方法中调用用例函数
    msg = pytest.raises(ZeroDivisionError, func)
    assert 'division by zero' in str(msg.value)
