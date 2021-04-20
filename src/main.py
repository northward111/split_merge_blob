from src.config import config
from src.utils.logger import Logger
from src.file_operation_base import FileOperationBase


def main():
    Logger.get_shared_logger().info('main invoked')
    Logger.get_shared_logger().info(config)
    operator = FileOperationBase(config["src"], config["des"], config["chunk_size"])
    if config["split"]:
        operator.split_file()
    else:
        operator.merge_file()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
