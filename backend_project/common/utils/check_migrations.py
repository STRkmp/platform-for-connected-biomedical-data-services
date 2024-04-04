import sys

migration_commands = ['flush', 'migrate', 'startapp', 'makemigrations']

def is_migrations():
    # Проверяем, что в списке аргументов командной строки есть ключ
    for command in migration_commands:
        if command in sys.argv:
            return True
    return False
