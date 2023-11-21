import asyncio
import time

async def fun4(x):
    print(time.strftime('%X'), "- fun4 начало")
    print(x**2)
    #print(asyncio.get_event_loop())
    #print(asyncio.get_running_loop())
    #if (asyncio.get_event_loop() == asyncio.get_running_loop()):
    #    print("loops are equal")
    await asyncio.sleep(3)
    print(time.strftime('%X'), "- fun4 завершена")

async def fun3(x):
    all_tasks = asyncio.all_tasks()
    #[print(task) for task in all_tasks]
    print("count tasks: ",len(all_tasks))
    print(time.strftime('%X'), "- fun3 начало")
    #print(x**2)
    #print(asyncio.get_event_loop())
    #print(asyncio.get_running_loop())
    #if (asyncio.get_event_loop() == asyncio.get_running_loop()):
    #    print("loops are equal")
    task4 = asyncio.create_task(fun4(x))
    all_tasks = asyncio.all_tasks()
    #[print(task) for task in all_tasks]
    print("count tasks: ",len(all_tasks))
    print(time.strftime('%X'), "- fun3 завершена")

async def main():
    print("-------------------------------")
    all_tasks = asyncio.all_tasks()
    #for task in all_tasks:
    #    print(task)
    #[print(task) for task in all_tasks]
    print("count tasks: ",len(all_tasks))
    #print("Loops: ")
    #print(asyncio.get_event_loop())
    #print(asyncio.get_running_loop())
    #if (asyncio.get_event_loop() == asyncio.get_running_loop()):
    #    print("loops are equal")
    task1 = asyncio.create_task(fun3(10))
    
    # Получаем все задачи в цикле событий
    all_tasks = asyncio.all_tasks()
    #[print(task) for task in all_tasks]
    print("count tasks: ",len(all_tasks))

    #await asyncio.gather(*asyncio.all_tasks())

    # Получаем все задачи в цикле событий после завершения main
    #all_tasks = asyncio.all_tasks()
    #[print(task) for task in all_tasks]
    #print("count tasks: ", len(all_tasks))

    print("-------------------------------")

asyncio.run(main(), debug=True)