import mysql.connector as mysql
from mysql.connector import Error

class DataRede:
    def staringConection(name:str,email:str,text:str) -> None:

        sql_fomart = '(' + '\'' + name + '\'' +',\'' + email + '\'' ',\'' + text + '\'' + ')'

        sqlCode = """INSERT INTO clientes(NameUser,EmailUser,DescriptionUser)
                    VALUE
            """
        
        sql = sqlCode + sql_fomart

        try:
            rede = mysql.connect(host='localhost',
                            database='formularioData',
                            user='root',
                            password='1234_dataBase')

            cursor = rede.cursor()
            cursor.execute(sql)
            rede.commit()
            cursor.close()
        except Error as e:
            print(f'Error data sent, type of error: {e}')
        finally:
            if (rede.is_connected()):
                rede.close()
