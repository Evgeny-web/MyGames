from psycopg2 import pool


def create_pool_connection(minconn, maxconn, host, user, password, db_name, port):
    # подключимся к нашей базе данных и создадим пул соединений
    connection_pool = pool.SimpleConnectionPool(
        minconn=minconn,
        maxconn=maxconn,
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )

    if connection_pool:
        print("Пул соединений успешно создан!")

    return connection_pool


def check_server_version(connection_pool: pool.SimpleConnectionPool):
    # получено соединение из пула
    connection = connection_pool.getconn()

    # Создадим курсор для выполнения запросов к бд
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server verstion: {cursor.fetchone()}")

    connection_pool.putconn(connection)
    # print("Соединение возвращено в пул")


def insert_nickname(connection_pool: pool.SimpleConnectionPool,
                       nickname: str):
    """
    Функиця для добавления никнейма пользователя в БД
    :param connection_pool: Пул соединений
    :param nickname: Имя пользователя
    """

    # получено соединение из пула
    connection = connection_pool.getconn()

    # Создадим курсор для выполнения запросов к бд
    with connection.cursor() as cursor:
        cursor.execute(
            f"INSERT INTO users (nickname) VALUES ({nickname})"
        )

        # Сохранили изменения в БД
        connection.commit()
    # Вернули соединение в пул
    connection_pool.putconn(connection)


def insert_snake_score(connection_pool: pool.SimpleConnectionPool,
                       score: str):
    """
    Сохраяем счет игрока в игре змейка в БД.
    :param connection_pool: Пул соединений
    :param score: Счет в игре
    """

    # получено соединение из пула
    connection = connection_pool.getconn()

    # Создадим курсор для выполнения запросов к бд
    with connection.cursor() as cursor:
        cursor.execute(
            f"INSERT INTO snake_scores () VALUES ({nickname})"
        )

        # Сохранили изменения в БД
        connection.commit()
    # Вернули соединение в пул
    connection_pool.putconn(connection)