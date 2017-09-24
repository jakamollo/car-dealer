#!python

# import modules here
import cgi, cgitb, database_connection, os,json
cgitb.enable()
# cgitb.enable()

# print("Content-type:text/html\r\n\r\n");
print("Content-type:text/html\n\n");

# create an instance of FieldStorage
data = cgi.FieldStorage()
print(data);
# get form values
product_id = data['product_id'].value
name = data['name'].value
model = data['model'].value
model_no = data['model_no'].value
color = data['color'].value
price = data['price'].value
price_currency = data['price_currency'].value
contacts = data['contacts'].value
country_of_origin = data['country_of_origin'].value
distance_covered = data['distance_covered'].value
engine_size = data['engine_size'].value
manufacturer = data['manufacturer'].value
year = data['year'].value
photo_file = data['photo']

success_message = ''
failure_message = ''
# check if the photo was uploaded
if photo_file.name:
	
	# store the photo to the images folder in the server
	original_file_name = photo_file.filename
	
	open('images/'+original_file_name, 'wb').write(photo_file.file.read())

	# now save the product to the database
	database_photo = 'images/'+ original_file_name
	database_connection.cur.execute('UPDATE PRODUCT set name=%s,model=%s,model_no=%s,color=%s,price=%s, \
		price_currency=%s,contacts=%s,country_of_origin=%s,distance_covered=%s,engine_size=%s,manufacturer=%s,year=%s,photo=%s where id=%s'\
		,(name,model,model_no,color,price,price_currency,contacts,country_of_origin,distance_covered,engine_size,manufacturer,year,database_photo,product_id,))
	success_message = 'Product successfully updated'

	# commit and close the database connection
	database_connection.conn.commit()
	database_connection.conn.close()
else:
	failure_message = 'Sorry, the product was not added'
