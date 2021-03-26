import os
from shutil import copyfile
import datetime
from src.utils.logger import Logger

input_dir = r'D:\data\download\导出的条目\files'
output_dir = r'D:\data\download\output{}'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

if not os.path.exists(output_dir):
    os.mkdir(output_dir)


def main():
    Logger.get_shared_logger().info('main invoked')
    for sub_folder_name in os.listdir(input_dir):
        for file in os.listdir(os.path.join(input_dir, sub_folder_name)):
            copyfile(os.path.join(input_dir, sub_folder_name, file), os.path.join(output_dir, file))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
