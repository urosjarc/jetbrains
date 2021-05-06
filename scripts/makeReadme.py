#!/usr/bin/python
# -*- coding: utf-8 -*-


class Readme(object):

    template = \
        """
# jetbrains
Settings for all JetBrains IDE-s

## Requirements
Command:
 - zip
 - unzip
 - meld

## Makefile
## Plugins
## Keymaps
	"""

    def __init__(self, path):
        self.__data = None
        self.__path = path

        self.__setData()
        pass

    @property
    def data(self):
        return '\n'.join(self.__data)

    @property
    def path(self):
        return self.__path

    def __setData(self):
        self.__data = Readme.template.split('\n')

    def __addDataText(
        self,
        lineString,
        arrayText,
        lineStringMethod,
        ):

        newDataArray = []

        for line in self.__data:
            newDataArray.append(line)
            if line == lineString:
                newDataArray.append('')
                for i in range(len(arrayText)):
                    newDataLine = lineStringMethod(arrayText, i)
                    if newDataLine:
                        newDataArray.append(newDataLine)

                newDataArray.append('')

        self.__data = newDataArray

    def update(self):
        with open(self.__path, 'w') as f:
            f.write(self.data)

    def addMakefile(self, addToreadmeHeader, path):
        with open(path) as f:
            makefile = f.readlines()

        def lineStringMethod(arrayText, i):
            lineArray = arrayText[i].split()
            if lineArray:
                if lineArray[0] == '@echo':

                    return '\t{}'.format(' '.join(lineArray[1:]).replace('"'
                            , ''))

        self.__addDataText(addToreadmeHeader, makefile,
                           lineStringMethod)

    def addKeymaps(self, addToreadmeHeader, path):
        with open(path) as f:
            keymaps = f.readlines()

        def lineStringMethod(arrayText, i):

            keyActionLine = arrayText[i].split('"')

            if keyActionLine[0].strip() == '<action id=':
                if keyActionLine[2].strip() == '>':
                    keystroke = arrayText[i + 1].split('"')[1]  # Keystroke
                else:
                    keystroke = ''

                return '\t{} {}'.format((keyActionLine[1] + ' '
                        ).ljust(35, '.'), keystroke)  # Actionname

        self.__addDataText(addToreadmeHeader, keymaps, lineStringMethod)

    def addPlugins(
        self,
        addToreadmeHeader,
        path,
        skip,
        ):
        with open(path) as f:
            installed = f.readlines()

        def lineStringMethod(arrayText, i):
            installedLine = arrayText[i].replace('\n', '')

            if not installedLine in skip:
                return ' - {}'.format(installedLine)

        self.__addDataText(addToreadmeHeader, installed,
                           lineStringMethod)


if __name__ == '__main__':
    readme = Readme(path='../README.md')
    readme.addMakefile(addToreadmeHeader='## Makefile',
                       path='../Makefile')
    readme.addKeymaps(addToreadmeHeader='## Keymaps',
                      path='../src/keymaps/XWin copy.xml')
    readme.addPlugins(addToreadmeHeader='## Plugins',
                      path='../src/installed.txt', skip=['intellij'
                      ])
    readme.update()
