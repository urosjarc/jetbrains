import os.path

class Readme(object):

	template = """
#PRO.Intellij
Settings for all Intellij IDE-s

##Requirements
Command:
 - zip
 - unzip
 - meld

##Makefile
##Keymap

	"""

	def __init__(self,path):
		self.__path = path
		self.__data = None

		self.__setData()

	@property
	def data(self):
		return self.__data

	@property
	def path(self):
		return self.__path

	def __setData(self):
		with open(os.path.join('..',self.__path)) as f:
			self.__data = f.readlines()

	def addMakefile(self,addToreadmeHeader,path):
		with open(os.path.join('..',path)) as f:



if __name__ == "__main__":
	readme = Readme(path='README.md')



