import aiohttp
import icalendar
from datetime import datetime, timezone, timedelta
import asyncio

import tracemalloc
tracemalloc.start()

ical_url = "https://calendar.google.com/calendar/ical/13bef4d0edd1d5deb6e5a6f382512d0b429e27d13417f02fb718d4b784d374f8%40group.calendar.google.com/private-2b4009c6d477a0fcfe67a553ee28e4ed/basic.ics"

previous_events = {}

async def fetch_ical_cycle(session, url, stop_session_event):
    while not stop_session_event.is_set():
        async with session.get(url) as response:
            print(response)

        # Ждем некоторое время перед следующей итерацией
        await asyncio.sleep(20)
    
    
    async with session.get(url) as response:
            ical_text = await response.text()
    process_events(ical_text)

def process_events(ical_text):
    calendar = icalendar.Calendar.from_ical(ical_text)
    now = datetime.now(timezone.utc)

    # Удаление событий, которые уже начались
    previous_events_copy = previous_events.copy()
    for uid, event in previous_events_copy.items():
        start_time = event.get("dtstart").dt
        if start_time < now:
            previous_events.remove(uid)

    for event in calendar.walk("vevent"):
        start_time = event.get("dtstart").dt
        time_until_event = start_time - now

        # Если событие еще не началось и его не было ранее
        if time_until_event.total_seconds() > 0 and event.get("UID") not in previous_events:
            print(f"Событие: {event.get('UID')}")
            print(f"Событие: {event.get('summary')}")
            print(f"Время начала: {start_time}")
            print(f"Осталось времени: {time_until_event}")

            # Добавляем событие в множество предыдущих событий
            previous_events[event.get("UID")] = event

async def main():
    try:
        
    async with aiohttp.ClientSession() as session:
        url = ical_url
        stop_session_event = asyncio.Event()
        print("Calendar monitoring is started")
        try:
            fetch_ical_connection = asyncio.create_task(fetch_ical_cycle(session, url, stop_session_event))
            #process_events(ical_text)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        
        
        # Ждем некоторое время, затем останавливаем выполнение
        await asyncio.sleep(1)
        stop_session_event.set()

        # Дожидаемся завершения выполнения HTTP-запросов
        await fetch_ical_connection
        print("Calendar monitoring is finished")
        
        

if __name__ == "__main__":
    asyncio.run(main())