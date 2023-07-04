# Напиши программу, которая одновременно читает несколько файлов, используя асинхронный файловый ввод-вывод.
# Программа должна считывать содержимое каждого файла и распечатывать их по мере их появления.

import asyncio
import aiofiles

async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
        print(f'Content of file {file_path}:')
        print(content)
        print()

async def read_files(file_paths):
    tasks = []
    for file_path in file_paths:
        task = asyncio.create_task(read_file(file_path))
        tasks.append(task)
    await asyncio.gather(*tasks)

async def main():
    file_paths = [
        r'C:\Users\danil\OneDrive\Рабочий стол\asyn\1.txt',
        r'C:\Users\danil\OneDrive\Рабочий стол\asyn\2.txt',
        r'C:\Users\danil\OneDrive\Рабочий стол\asyn\3.txt'
    ]
    await read_files(file_paths)

asyncio.run(main())
