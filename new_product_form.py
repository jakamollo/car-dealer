#!python

# import modules
import footer, nav, js_includes, css_includes
 	
print("Content-type:text/html\r\n\r\n");
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

print('Price : <input style="margin-left:155px; margin-bottom:10px;" type="text" name="price" required/><br>');

print('Price Currency : <input style="margin-left:90px; margin-bottom:10px;" type="text" name="price_currency" required/><br>');

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