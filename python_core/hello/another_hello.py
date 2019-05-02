import python_core.hello.hello
from python_core.utils import file_handling_util


def hello(msg):
    print('Hello in another_hello.py from ' + msg)


if __name__ == '__main__':
    current_module_name = file_handling_util.get_file_name_from_path(__file__)
    hello(current_module_name)
else:
    hello("some another hello py")
