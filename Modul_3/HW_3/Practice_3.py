# Напиши программу, которая одновременно читает несколько файлов, используя асинхронный файловый ввод-вывод.
# Программа должна считывать содержимое каждого файла и распечатывать их по мере их появления.

import asyncio
import aiofiles

async def read_file(file_path):
    try:
        async with aiofiles.open(file_path, mode='r') as file:
            content = await file.read()
            print(f'Content of file {file_path}:')
            print(content)
            print()
    except FileNotFoundError:
        print(f'File {file_path} not found.')
    except Exception as e:
        print(f'Error occurred while reading file {file_path}: {str(e)}')

async def read_files(file_paths):
    tasks = []
    for file_path in file_paths:
        task = asyncio.create_task(read_file(file_path))
        tasks.append(task)
    await asyncio.gather(*tasks)

async def main():
    file_paths = [
        r'1',
        r'2',
        r'3'
    ]
    await read_files(file_paths)

try:
    asyncio.run(main())
except Exception as e:
    print(f'Error occurred: {str(e)}')

