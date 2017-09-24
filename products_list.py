#!python

# import modules here
import cgi, cgitb, database_connection, footer, nav, js_includes, css_includes,base64
import edit_product

database_connection.cur.execute('SELECT * from product')
product_list = database_connection.cur.fetchall()

product_row = []

print("Content-type:text/html\r\n\r\n");
print('<html>');
print('<head>');
print('<meta charset="utf-8">');
print('<title>');
print('Cad Dealer - List of Products');
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
# beginning of user list div
print('<div class = "update-user-list-div">');
print('<h3 style="padding-left: 30px;font-style:italic;margin-top:10px;"">List of Products</h3>');
# define message area
print('<div class = "message-div"></div>');
print('-----------------------------------------------------------------------------------------------------------------------------------');
# product section div
if len(product_list) > 0:
	for product_row in product_list:
		# product data
		product_id = product_row[0]
		manufacturer = product_row[1]
		name = product_row[2]
		color = product_row[3]
		country_of_origin = product_row[4]
		price = product_row[12]
		price_currency = product_row[13]
		year = product_row[5]
		engine_size = product_row[6]
		contacts = product_row[7]
		distance_covered = product_row[8]
		photo = product_row[9]
		model = product_row[10]
		model_no = product_row[11]

		data_uri = base64.b64encode(open(photo, 'rb').read()).decode('utf-8').replace('\n', '')
		img_tag = '<img src="data:image/png/jpg/jif;base64,{0}" width="250" height="180">'.format(data_uri)
		edit_product.edit_product(product_id,name,model,model_no,color,contacts,country_of_origin,distance_covered,engine_size,manufacturer,year,price,price_currency)
        
		print(
			
			'<div class = "product_list_div" id ="pdct_lst_%d" style = "width:790; height:250px;margin-bottom:0px;margin-left:20px;">'
			'%s'
	        
	        '<div class = "product_data_div" style="position:relative;left:280px;top:-170px;">'
	        '<p style="margin-bottom:0px;"><span style="font-style:italic;font-weight:bold;">Name:</span> %s   <span style="font-style:italic;font-weight:bold;">Contacts:</span> %s</p>'
	        '<p style="margin-bottom:0px;"><span style="font-style:italic;font-weight:bold;">Manufacturer:</span> %s  <span style="font-style:italic;font-weight:bold;">Distance Covered:</span> %d Km(s)</p>'
	        '<p style="margin-bottom:0px;"><span style="font-style:italic;font-weight:bold;">Color:</span> %s  <span style="font-style:italic;font-weight:bold;">Model:</span> %s</p>'
	        '<p style="margin-bottom:0px;"><span style="font-style:italic;font-weight:bold;">Country of Origin:</span> %s  <span style="font-style:italic;font-weight:bold;">Model Number:</span> %s</p>'
	        '<p style="margin-bottom:0px;"><span style="font-style:italic;font-weight:bold;">Year of Manufacture:</span> %d  <span style="font-style:italic;font-weight:bold;">Price: </span>%s: %d</p>'
	        '<p style="margin-bottom:0px;"><span style="font-style:italic;font-weight:bold;">Engine Size:</span> %s</p>'
	        '<p>'
	        '<button class = "btn btn-primary" id = "edit-user-%d" data-toggle = "modal" data-target = "#%d">Edit</button>'
	        '<button value = "%d" class = "btn btn-danger delete-pdct" id = "delete-pdct-%d">Delete</button>'
	        '</p>'
	        '</div>'
	        '</div>'
	        %(product_id,img_tag,name,contacts,manufacturer,distance_covered,color,model,country_of_origin,model_no,year,price_currency,price,engine_size,product_id,product_id,product_id,product_id)
			);
        
else:
	print(
		'<div style = "background-color:lightpink;height:40px;">No Product found</div>'
		);

print('<ul id="pagination-demo" class="pagination-sm"></ul>');
# users table

print('</div>');
# end of form div
# add the footer
footer.print_footer()
print('</div>');
print('</body>');
print('</html>');
