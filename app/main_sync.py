from dotenv import load_dotenv
import logging
import logging.config 
from os import path
from os import environ

import requests
import icalendar
from datetime import datetime, timedelta
import time

log_file_path = path.join(path.dirname(path.abspath(__file__)), '../logging_config.ini')
logging.config.fileConfig(log_file_path)

logger = logging.getLogger("dev")

# Загрузить переменные окружения из файла .env
load_dotenv()

# Замените "MY_ENV_VARIABLE" на имя вашей переменной окружения
SERVICE_ACCOUNT_FILE = environ.get("GOOGLE_SERVICE_ACCOUNT_FILE");

if SERVICE_ACCOUNT_FILE is not None:
    logger.info("Google service accaunt file detected.")
else:
    logger.error("Google service accaunt file detected!")



# URL закрытого адреса iCal
ical_url = "https://calendar.google.com/calendar/ical/13bef4d0edd1d5deb6e5a6f382512d0b429e27d13417f02fb718d4b784d374f8%40group.calendar.google.com/private-2b4009c6d477a0fcfe67a553ee28e4ed/basic.ics"

while True:
    # Запрос на закрытый адрес iCal
    response = requests.get(ical_url)
    calendar = icalendar.Calendar.from_ical(response.text)

    # Получение текущего времени
    now = datetime.utcnow()  # Make now offset-naive

    # Проверка событий
    for event in calendar.walk("vevent"):
        start_time = event.get("dtstart").dt
        start_time_naive = start_time.replace(tzinfo=None)  # Convert to offset-naive
        time_until_event = start_time_naive - now

        # Если до события осталось менее 15 минут, выводим информацию в консоль
        if time_until_event.total_seconds() <= 15 * 60:
            print(f"Событие: {event.get('summary')}")
            print(f"Время начала: {start_time}")
            print(f"Осталось времени: {time_until_event}")

    # Пауза перед следующим запросом
    time.sleep(10)

