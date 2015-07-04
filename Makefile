help:
	@echo "settings-jar - Create settings .jar file from global settings folder."

settings-jar:
	rm settings.jar
	cd settings/ && zip settings.jar * 
	mv settings/settings.jar .
