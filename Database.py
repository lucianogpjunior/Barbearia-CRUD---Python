import mariadb
import sys

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Mmf65@pch"
        self.database = "barbearia_db"

    def conectar_banco(self):
        try:
            return mariadb.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        except mariadb.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            sys.exit(1)