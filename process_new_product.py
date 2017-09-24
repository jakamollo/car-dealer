#!python

# import modules here
import cgi, cgitb, database_connection, footer, nav, js_includes, css_includes, os
cgitb.enable()

print("Content-type:text/html\r\n\r\n");
# create an instance of FieldStorage
form = cgi.FieldStorage()
# get form values
name = form.getvalue('name')
model = form.getvalue('model')
model_no = form.getvalue('model_no')
color = form.getvalue('color')
price = form.getvalue('price')
price_currency = form.getvalue('price_currency')
contacts = form.getvalue('contacts')
country_of_origin = form.getvalue('country_of_origin')
distance_covered = form.getvalue('distance_covered')
engine_size = form.getvalue('engine_size')
manufacturer = form.getvalue('manufacturer')
year = form.getvalue('year')
photo_file = form['photo']

success_message = ''
failure_message = ''
# check if the photo was uploaded
if photo_file.name:
	
	# store the photo to the images folder in the server
	original_file_name = photo_file.filename
	
	open('images/'+original_file_name, 'wb').write(photo_file.file.read())

	# now save the product to the database
	database_photo = 'images/'+ original_file_name
	database_connection.cur.execute('INSERT INTO product(color,contacts,country_of_origin,price,price_currency, \
		distance_covered,engine_size,manufacturer,model,model_no,name,photo,year) VALUES(%s,%s, \
		%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(color,contacts,country_of_origin,price,price_currency,distance_covered,engine_size,\
		manufacturer,model,model_no,name,database_photo,year))
	success_message = 'Product successfully added to the database'

	# commit and close the database connection
	database_connection.conn.commit()
	database_connection.conn.close()
else:
	failure_message = 'Sorry, the product was not added'

print('<html>');
print('<head>');
print('<meta charset="utf-8">');
print('<title>');
print('Cad Dealer - New Product');
print('</title>');
# include js sources
js_includes.js_includes()

# include css sources
css_includes.css_includes()
print('</head>');
print('<body>');
print('<div class="car-home-wrapper">');
# add the navigation
nav.print_nav()

# beginning of form div
print('<div class = "new-product-form-div">');
print('<h3 style="padding-left: 30px;">Add New Product</h3>');
# define message area
print('<div class = "message-div"></div>');
# display sussess message if the product was successfully added
if success_message != '':
	print(
		'<p class = "message-div" style="height:35px;background-color:lightgreen;">'+success_message+'</p>'
		);
# display failure message if the product was not added
if failure_message != '':
	print(
		'<div style="height:35px;background-color:lightpink;"><p style="padding-left:5px;">'+failure_message+'</p></div>'
		);
print('<form action="/cgi-bin/car_dealer/process_new_product.py" method="post" class = "new_product_form" enctype="multipart/form-data">');
print('Product Name: <input style="margin-left:88px; margin-bottom:10px;" type="text" name="name" required/><br>');

print('Model: <input style="margin-left:145px; margin-bottom:10px;" type="text" name="model" required/><br>');

print('Model Number: <input style="margin-left:83px; margin-bottom:10px;" type="text" name="model_no" required/><br>');

print('Color: <input style="margin-left:150px; margin-bottom:10px;" type="text" name="color" required/><br>');

print('Contacts : <input style="margin-left:125px; margin-bottom:10px;" type="text" name="contacts" required/><br>');

print('Country of Origin : <input style="margin-left:65px; margin-bottom:10px;" type="text" name="country_of_origin" required/><br>');

print('Distance Covered : <input style="margin-left:65px; margin-bottom:10px;" type="text" name="distance_covered" required/><br>');

print('Engine Size : <input style="margin-left:105px; margin-bottom:10px;" type="text" name="engine_size" required/><br>');

print('Manufacturer : <input style="margin-left:90px; margin-bottom:10px;" type="text" name="manufacturer" required/><br>');

print('Year of Manufacture : <input style="margin-left:47px; margin-bottom:10px;" type="text" name="year" required/><br>');

print('Product Photo : <input class = "btn btn-primary" style="margin-left:87px; margin-bottom:10px;" type="file" name="photo" required/><br>');
print('<button class = "btn btn-primary new-user-submit-button" type="submit">Submit Product</button>');
print('</form>');
print('</div>');
# end of form div
# add the footer
footer.print_footer()
print('</div>');
print('</body>');
print('</html>');

