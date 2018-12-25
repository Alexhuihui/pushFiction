# -*- coding:utf-8 -*-
import configparser


class ParserConfig:
	
	def __init__(self):
		self.cf = configparser.ConfigParser()
	
	def readValueFromPath(self, path, section, option):
		self.cf.read(path)
		return self.cf.get(section=section, option=option)
	
	def readSections(self, path):
		self.cf.read(path)
		return self.cf.sections()


if __name__ == '__main__':
	parser = ParserConfig()
	test = parser.readValueFromPath("./configParser.conf", "db", "db")
	print(test)
	print(parser.readSections("./configParser.conf"))
