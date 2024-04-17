bash:
	docker exec -it iot-commands-hub-app-1 bash

debug:
	docker attach iot-commands-hub-app-1

python_shell:
	docker exec -it iot-commands-hub-app-1 bash -c "python manage.py shell"

migrate:
	docker exec iot-commands-hub-app-1 bash -c "python manage.py makemigrations && python manage.py migrate"