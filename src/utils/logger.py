import logging
import logging.handlers
import os


class Logger:
    @classmethod
    def get_shared_logger(cls):
        return Logger("default").get_log()

    def __init__(self, logger_name):
        # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        self.logger.handlers.clear()
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        logs_path = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)
        log_path = os.path.join(logs_path, "%s.log" % logger_name)
        fh = logging.handlers.RotatingFileHandler(log_path, encoding="utf8", maxBytes=100000, backupCount=3, mode="w")
        fh.setLevel(logging.INFO)

        # 创建一个handler，用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger
