help:
	@echo "settings - Create settings .zip file from global settings folder."
	@echo "diff     - Diff .zip file with global settings folder."
	@echo "clean        - Clean not used elements."
	@echo "install      - Create settings .jar file and update README.md"
	@echo "readme       - Update README.md file"

install:
	$(MAKE) settings
	$(MAKE) readme

diff:
	rm tmp -rf
	mkdir tmp
	cp ./settings.zip tmp
	cd tmp && unzip *.zip
	rm tmp/*.zip
	meld src tmp
	rm tmp -rf

readme:
	cd scripts && python3 makeReadme.py

settings:
	cd src/ && zip -r my-settings.zip *
	mv src/my-settings.zip .

clean:
	rm tmp* -rf
	rm *.zip
	


