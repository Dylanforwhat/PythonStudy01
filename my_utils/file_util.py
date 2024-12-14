"""
文件相关自定义工具

"""
def print_file_info(file_name):
    """
    将给定路径的文件内容输出到控制台中
    :param file_name:将要读取的文件路径
    :return:None（直接输出控制台）
    """
    f =None
    try:
        f= open(file_name,"r",encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(f"出现异常，异常原因：{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    """
    将指定的数据追加到指定的文件中
    :param file_name:指定文件的路径
    :param data:指定的数据
    :return:None
    """
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    # print_file_info("d:/bill.txt")
    append_to_file("d:/bill.txt","xiaohong 2000")