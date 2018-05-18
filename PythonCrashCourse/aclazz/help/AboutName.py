#需要测试的方法
def get_format_name(frist_name,last_name,midd_name=''):
    if midd_name:
        name = frist_name + " " + midd_name + " " + last_name
    else:
        name = frist_name + " " + last_name
    return name
