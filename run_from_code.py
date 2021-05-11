"""
直接从python代码中运行用例
"""
import pytest


class MyPlugin:

    def pytest_sessionfinish(self):
        print('*** test run reporting finishing')


if __name__ == '__main__':
    pytest.main(['-qq', './'], plugins=[MyPlugin()])
