"""
可以通过多种方式执行要执行的用例
1. 通过 pytest test_xxx.py指定文件
2. 通过 pytest test_dir/指定文件夹中的所有文件
3. 通过 pytest -k "Cases and not two"将运行除了test_two以外的所有TestCases中的用例
4. 通过 pytest test_xxx.py::TestCases可以执行指定类/函数中的用例
5. 通过 pytest test_xxx.py::TestCases::test_two可以执行指定类方法
5. 通过 pytest -m slow可以执行当前目录中所有被标记为slow的用例
6. 通过 pytest --pyargs pkg.testing可以导入python包中的用例进行执行
"""
import time

import pytest


class TestCases:

    def test_one(self):
        assert 1

    def test_two(self):
        assert 0

    @pytest.mark.slow
    def test_three(self):
        time.sleep(2)
        assert 'a' in 'b'
