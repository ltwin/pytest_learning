"""
pytest提供了内置的参数，使用pytest --fixtures获取所有可用参数
"""


def test_tmp_path(tmp_path):
    """
    用于获取一个随机且唯一的临时路径，
    同一个用例的路径是固定的，如该用例为test_tmp_path0
    """
    print(tmp_path)
    assert 0
