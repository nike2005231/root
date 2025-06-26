import sqlite3

class DataBase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()    

    #Закрываем соединение
    def close(self):
        self.cursor.close()
        self.conn.close()

    #Получаем данные
    def get_data(self, *params, request):
        try:
            self.cursor.execute(request, params)
            return self.cursor.fetchall()

        except Exception as ex:
            print(f"{ex}")

    #Передаем данные
    def insert_data(self, *params, request, mes_debug=None):
        try:
            self.cursor.execute(request, params)
            self.conn.commit()
            if mes_debug:
                print(mes_debug)
        except Exception as ex:
            print(f"{ex}")
