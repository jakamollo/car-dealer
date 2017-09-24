#!python

def print_nav():
	nav_div = print(
		'<div class = "nav-div">'
		'<ul class = "nav-ul">'
		'<li><a href="/cgi-bin/car_dealer/home.py">Home</a></li>'
		'<li><a href="/cgi-bin/car_dealer/home.py">Products</a>'
		'<ul>'
		'<li><a href="/cgi-bin/car_dealer/products_list.py">Products List</a></li>'
		'<li><a href="/cgi-bin/car_dealer/home.py">Sold Products</a></li>'
		'<li><a href="/cgi-bin/car_dealer/home.py">New Arrivals</a></li>'
		'</ul>'
		'</li>'
		'<li><a href="/cgi-bin/car_dealer/home.py">Contacts</a></li>'
		'<li><a href="/cgi-bin/car_dealer/home.py">About</a></li>'
		'<li><a href="/cgi-bin/car_dealer/home.py">Terms of Trade</a></li>'
		'<li><a href="#">Administration</a>'
		'<ul>'
		'<li><a href="/cgi-bin/car_dealer/new_user.py">Add Users</a></li>'
		'<li><a href="/cgi-bin/car_dealer/update_user.py">Update User</a></li>'
		'<li><a href="/cgi-bin/car_dealer/home.py">Delete User</a></li>'
		'<li><a href="/cgi-bin/car_dealer/new_product_form.py">Add Product</a></li>'
		'</ul>'
		'</li>'
		'</ul>'
		'</div>'
		);
	return nav_div