#!python

# import modules
import database_connection, cgi, cgitb, json

def delete_user_record():
	status = ''
	message = ''
	data = cgi.FieldStorage()

	user_id = data['user_id'].value

	database_connection.cur.execute('DELETE from USERS where id = %s',(user_id,))
	database_connection.conn.commit()
	

delete_user_record()

print("Content-type:text/html\n\n");

