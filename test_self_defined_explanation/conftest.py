from test_foo_compare import Foo


def pytest_assertrepr_compare(op, left, right):
    """
    自定义用例失败信息，替换的内容为“E xxx==xxx”部分
    :param op: 操作符，如“assert a == b”的操作符就是“==”
    :param left: 操作符左边的对象
    :param right: 操作符右边的对象
    :return:
    """
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return [
            'Comparing Foo instances:',
            f'  vals: {left.val} != {right.val}'
        ]
