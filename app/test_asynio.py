import asyncio
import time

def fun1(x):
    print(time.strftime('%X'), "- fun1 начало")
    print (x**3)
    time.sleep(3)
    print(time.strftime('%X'), "- fun1 завершена")
    
async def fun2(x):
    print(time.strftime('%X'), "- fun2 начало")
    print(x**2)
    # time.sleep(3)
    #await asyncio.sleep(3)
    #asyncio.create_task(asyncio.sleep(3))
    fun2_loop = asyncio.get_event_loop()
    fun2_loop.set_debug(True)
    print(fun2_loop._thread_id)
    asyncio.create_task(fun4(x))
    print(time.strftime('%X'), "- fun2 завершена")


async def fun4(x):
    print(time.strftime('%X'), "- fun4 начало")
    print(x**2)
    #asyncio.create_task(asyncio.sleep(3))
    #await asyncio.sleep(3)
    time.sleep(3)
    print(time.strftime('%X'), "- fun4 завершена")

async def fun3(x):
    print(time.strftime('%X'), "- fun3 начало")
    print(x**2)
    #asyncio.create_task(asyncio.sleep(3))
    #await asyncio.sleep(3)
    task4 = asyncio.create_task(fun4(x))
    #await fun4(x)
    # Получаем все задачи в цикле событий
    all_tasks = asyncio.all_tasks()
    print(all_tasks)
    #await task4
    print(time.strftime('%X'), "- fun3 завершена")

"""
async def fun4(x):
    with open("fun4_out.txt", "a") as f:
        f.write(''.join([time.strftime('%X'), "- fun4 начало", "\n"]))
        f.write(str(x**2))
        f.write("\n")
        await asyncio.sleep(3)
    #await asyncio.sleep(3)
        f.write(''.join([time.strftime('%X'), "- fun4 завершена", "\n"]))
"""
async def main():
    print("-------------------------------")
    all_tasks = asyncio.all_tasks()
    print(len(all_tasks))
    task1 = asyncio.create_task(fun3(10))
    #all_tasks = asyncio.all_tasks()
    #print(len(all_tasks))
    #task2 = asyncio.create_task(fun2(5))
    
    #fun1(5)
    #main_loop = asyncio.get_event_loop()
    #main_loop.set_debug(True)
    # Получаем все задачи в цикле событий
    all_tasks = asyncio.all_tasks()
    print(len(all_tasks))
    #print(main_loop._thread_id)   

    # await task1, task2

    #await fun4(16)
    #await asyncio.sleep(0)
    print("-------------------------------")

asyncio.run(main(), debug=True)
"""
loop = asyncio.get_event_loop()
task1 = loop.create_task(fun1(4))
task2 = loop.create_task(fun2(4))
loop.run_until_complete(asyncio.wait([task1, task2]))
"""
"""
async def fun3(x):
    #print(x**0.5)
    await asyncio.sleep(3)
    #print('fun2 завершена')

async def main():
    



    #await fun1(4)
    #await fun2(4)

    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    #print(type(task1))
    #print(task1.__class__.__bases__)
    #print(type(await task1))
    #print("-------------------------------")
    print(type(fun1))
    print(type(fun1(4)))
    #print(type(await fun1(4)))
    #print("-------------------------------")
    #print(type(fun3))
    #print(type(fun3(4)))
    #print("-------------------------------")

    await asyncio.sleep(10)
    #await task2


asyncio.run(main())

"""