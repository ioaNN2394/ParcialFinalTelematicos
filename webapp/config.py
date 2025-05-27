class Config:
    MYSQL_HOST = '192.168.60.3' 
    MYSQL_USER = 'root'        
    MYSQL_PASSWORD = 'root'    
    MYSQL_DB = 'myflaskapp'
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
