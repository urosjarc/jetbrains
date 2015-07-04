help:
	@echo "settings - Create settings .jar file from global settings folder."

settings.jar:
	cd settings/ && zip settings.jar *
	mv settings.jar ..
