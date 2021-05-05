build:
	docker build --force-rm $(options) -t patient-managment:latest 
build-prod:
	$(MAKE) build options="--target production"
compose-start:
	docker-compose up --remove-orphins $(options)
compose-stop:
	docker-compose down --remove-orphins $(options)
compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd)