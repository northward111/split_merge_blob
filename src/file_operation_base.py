import os


def cmp(x):
    return int(os.path.splitext(x)[1].replace(".", ""))


class FileOperationBase:
    def __init__(self, src_path, des_path, chunk_size=1024 * 1024):
        self.chunk_size = chunk_size

        self.src_path = src_path
        self.des_path = des_path

    def split_file(self):
        # 'split the files into chunks, and save them into des_path'
        if not os.path.exists(self.des_path):
            os.mkdir(self.des_path)
        chunk_num = 0
        input_file = open(self.src_path, 'rb')  # rb 读二进制文件
        try:
            while 1:
                chunk = input_file.read(self.chunk_size)
                if not chunk:  # 文件块是空的
                    break
                chunk_num += 1
                filename = os.path.join(self.des_path,
                                        "%s.%d" % (os.path.split(self.src_path)[1], chunk_num))
                file_obj = open(filename, 'wb')
                file_obj.write(chunk)
        except IOError:
            print("read file error\n")
            raise IOError
        finally:
            input_file.close()
            return chunk_num

    def merge_file(self):
        # '将src路径下的所有文件块合并，并存储到des路径下。'

        if not os.path.exists(self.src_path):
            print("src_path doesn't exists, you need a src_path")
            raise IOError
        files = os.listdir(self.src_path)
        files.sort(key=cmp)
        with open(self.des_path, 'wb') as output:
            for each_file in files:
                filepath = os.path.join(self.src_path, each_file)
                with open(filepath, 'rb') as infile:
                    data = infile.read()
                    output.write(data)

# a = "C:\Users\JustYoung\Desktop\unix报告作业.docx".decode('utf-8')
# test = FileOperationBase(a, "C:\Users\JustYoung\Desktop\SplitFile\est", 1024)
# test.splitFile()
# a = "C:\Users\JustYoung\Desktop\SplitFile\est"
# test = FileOperationBase(a, "out")
# test.mergeFile()
