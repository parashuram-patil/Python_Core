from python_core.utils import file_handling_util


def hello(msg):
    print('Hello in hello.py from ' + msg)


if __name__ == '__main__':
    current_module_name = file_handling_util.get_file_name_from_path(__file__)
    hello(current_module_name)
else:
    hello("another_hello.py")
