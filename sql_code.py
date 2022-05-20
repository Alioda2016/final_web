import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="stutter")
db_cursor = db_connection.cursor()


def insertuser(first_name, last_name, email, password):
    db_cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES(%s, %s, %s,%s)",
                      (str(first_name), str(last_name), str(email), str(password)))
    db_connection.commit()
    return True


def signin(email, password):
    result = ""
    db_cursor.execute("select email ,password from users where email=%s and password=%s", (str(email), str(password)))
    for sign in db_cursor:
        result = sign[0]
    if result != "":
        db_connection.commit()
        return 1
    else:
        db_connection.commit()
        return 0


def update_password(email, password):
    sql = "update users set password=%s where email=%s"
    value = (str(password), str(email))
    db_cursor.execute(sql, value)
    db_connection.commit()
    return True


def update_info(first_name, last_name, email, psw):
    sql = "update users set password=%s, first_name=%s, last_name=%s where email=%s"
    value = (str(psw), str(first_name), str(last_name), str(email))
    db_cursor.execute(sql, value)
    db_connection.commit()
    return True


def get_userdata(email, psw):
    db_cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, psw,))
    account = db_cursor.fetchone()
    db_connection.commit()
    return account

def delete_user(email):
    db_cursor.execute('DELETE FROM users where email = %s', (email,))
    account = db_cursor.fetchone()
    db_connection.commit()
    return account

def get_record_number(id):
    db_cursor.execute('SELECT count( * ) FROM audio_data WHERE id =%s', (id,))
    x = db_cursor.fetchone()
    db_connection.commit()
    return x


def insert_audio_data(id, audio_path, created_at):
    db_cursor.execute('INSERT INTO audio_data (id, audio_path, created_at) VALUES(%s, %s, %s)',
                      (id, audio_path, created_at))
    db_connection.commit()


def insert_score(audio_path, score):
    db_cursor.execute('UPDATE audio_data set score=%s WHERE audio_path=%s', (str(score), audio_path))
    db_connection.commit()


def get_graph_data(id):
    db_cursor.execute('SELECT sum(score),COUNT(score) FROM audio_data WHERE id=%s GROUP BY DATE(created_at)', (id,))
    x = db_cursor.fetchall()
    if len(x) == 0:
        return 0
    if None in x[0]:
        db_connection.commit()
        return 0
    else:
        y = [float(i[0] / i[1]) for i in x]
        db_cursor.execute('SELECT DISTINCT DATE(created_at) FROM audio_data WHERE id=%s AND score IS NOT NULL', (id,))
        dt = db_cursor.fetchall()
        if None in dt[0]:
            db_connection.commit()
            return 0
        else:
            dt = [w[0] for w in dt]
            db_connection.commit()
            return y, dt
    # print (y)
    # print (dt)
# insert_audio_data(4,'gjhg','2022-03-10 11:05:20')
# insert_score('gjhg',63.45)

# get_graph_data(5)
