#!python

# import modules
import database_connection, cgi, cgitb, json

def delete_product_record():
	status = ''
	message = ''
	data = cgi.FieldStorage()

	product_id = data['product_id'].value

	database_connection.cur.execute('DELETE from PRODUCT where id = %s',(product_id,))
	database_connection.conn.commit()
	

delete_product_record()

print("Content-type:text/html\n\n");