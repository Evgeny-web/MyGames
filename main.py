import psycopg2.pool

from AppSettings import *
from utils.db_data.db_funcs import *
from apps.Main_menu import main_menu
from apps.start_create_nickname import start_create_nickname

import psycopg2 as psg
from config import *

if __name__ == "__main__":
    try:
        # Создание пула соединений с БД перед запуском приложения
        connection_pool = create_pool_connection(1, 3, host, user, password, db_name, port)

        check_server_version(connection_pool)

        # Проверка на первый запуск
        check_first_entry(user_data_path, start_create_nickname)

        # Запуск приложения
        main_menu(connection_pool)

    except Exception as ex:
        print("[INFO] Error while working with PostgreSQL", ex)

    finally:
        if connection_pool:
            connection_pool.closeall()
            print("[INFO] PostgreSQL connection closed")
