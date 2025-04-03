import configparser


# 创建ConfigParser对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini',encoding='utf8')