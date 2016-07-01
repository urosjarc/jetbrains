help:
	@echo "settings-jar - Create settings .jar file from global settings folder."
	@echo "diff-jar     - Diff .jar file with global settings folder."
	@echo "diff-jars    - Diff 2 .jar files"
	@echo "clean        - Clean not used elements."
	@echo "install      - Create settings .jar file and update README.md"
	@echo "readme       - Update README.md file"

install:
	$(MAKE) settings-jar
	$(MAKE) readme

diff-jar:
	echo ">>> jar = $(jar) <<<"
	
	rm tmp -rf
	
	mkdir tmp
	cp $(jar) tmp
	cd tmp && unzip *.jar
	rm tmp/*.jar

	meld settings tmp
	
	rm tmp -rf

readme:
	cd scripts && python makeReadme.py

settings-jar:
	cd settings/ && zip -r settings.jar * 
	mv settings/settings.jar .

diff-jars:
	echo ">>> jar1 = $(jar1) <<<"
	echo ">>> jar2 = $(jar2) <<<"
	
	rm tmp* -rf
	
	mkdir tmp1
	cp $(jar1) tmp1
	cd tmp1 && unzip *.jar
	rm tmp1/*.jar
	
	mkdir tmp2
	cp $(jar2) tmp2
	cd tmp2 && unzip *.jar
	rm tmp2/*.jar
	
	meld tmp1 tmp2
	
	rm tmp* -rf

clean:
	rm tmp* -rf
	rm *.jar
	


