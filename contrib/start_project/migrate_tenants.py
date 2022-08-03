#! python3

import json
import os
import subprocess
import sys
import threading

DATABASES = {}
THREADS = []


def main():
    try:
        DATABASES = json.loads(os.environ.get("DATABASE_URLS", "{}"))

    except Exception as e:
        print("Erro ao processar a variável DATABASE_URLS")
        print(e)
        sys.exit(1)
    if not DATABASES:
        print(f"Variável DATABASE_URLS está vazia => {DATABASES}")
        with open(".env", "r") as file:
            env_ = file.readlines()
        for line in env_:
            if line.startswith("DATABASE_URLS"):
                DATABASES = json.loads(line.split("=", 1)[-1])
                break
    if not DATABASES:
        print("DATABASE_URLS não encontrado no .env")
        sys.exit(1)

    for item in DATABASES.items():
        THREADS.append(threading.Thread(target=migrate_process, args=item))

    for i in range(len(THREADS)):
        THREADS[i].start()
        THREADS[i].join()
    print("All done!")


def migrate_process(key, value):
    print(f"Starting migrations from tenant {key}")

    database = json.dumps({"default": value}, indent=4)
    subprocess.Popen(f"DATABASE_URLS='{database}' python manage.py migrate", shell=True)
    print(f"thread finished {key}...exiting")
    sys.exit(0)


if __name__ == "__main__":
    main()
