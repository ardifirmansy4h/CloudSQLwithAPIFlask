import os
import pymysql
from flask import jsonify, request


db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn


def get():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM growth;')
        grwth = cursor.fetchall()
        if result > 0:
            got_grwth = jsonify(grwth)
        else:
            got_grwth = 'Empty Database'
        return got_grwth


def create(grwt):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO growth (child_name, age_month, gender, child_height, child_weight, head_size, chest_size, belly_size, result, created_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (grwt["child_name"], grwt["age_month"], grwt["gender"], grwt["child_height"], grwt["child_weight"], grwt["head_size"], grwt["chest_size"], grwt["belly_size"], grwt["result"], grwt["created_at"],))
    conn.commit()
    conn.close()

def delete(id):
    conn = open_connection()
    with conn.cursor() as cursor:
         sql = 'DELETE FROM growth WHERE id = %s'
         cursor.execute(sql, id)
    conn.commit()
    conn.close()

 
    
    
        




    

 



