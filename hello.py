from utils import file_handling_util


def hello(msg):
    print('Hello from ' + msg)


if __name__ == '__main__':
    current_module_name = file_handling_util.get_file_name_from_path(__file__)
    hello(current_module_name)
