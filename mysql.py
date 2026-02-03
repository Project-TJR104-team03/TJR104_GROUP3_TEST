import pymysql

# 設定資料庫連線資訊
host = 'localhost'
port = 3306
user = 'root'
passwd = 'password'  #注意平常不會這樣用
db = 'TESTDB'
charset = 'utf8mb4'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)