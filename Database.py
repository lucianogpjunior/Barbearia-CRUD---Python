import mysql
import mysql.connector
import sys

class Database:
    def __init__(self, host, user, password, database):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "barbearia_db"

    def conectar_banco(self) -> None:
        try:
            return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
        sys.exit(1)