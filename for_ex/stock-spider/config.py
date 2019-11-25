import yaml

""" 
加载配置文件
"""


def load_config(file):
    with open("resources/" + file) as f:
        return yaml.load(f)
