# -*- coding:utf-8 -*-
from conf import readConfig

read = readConfig.ParserConfig()
path = "../conf/configParser.conf"

print(read.readValueFromPath(path, "db", "passwd"))
