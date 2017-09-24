#!python

# import modules
import footer, nav, js_includes, css_includes

print("Content-type:text/html\r\n\r\n");
print('<html>');
print('<head>');
print('<meta charset="utf-8">');
print('<title>Car Dealer Home</title>');
# include js sources
js_includes.js_includes()

# include css sources
css_includes.css_includes()
print('</head>');
print('<body class="">');
print('<div class="car-home-wrapper">');
# add the navigation
nav.print_nav()
print('<h3 style = "padding-left:40px;font-style:obligue;font-weight:bold;margin-top:10px;">Home of Machine Choices</h3>');
# featured div
print(
	'<div class = "home_featured">'
	'<h3>Featured Cars</h3>'
	'<img src = "/cgi-bin/car_dealer/images/bamba-box.png" width = "350px" height = "250px" alt = "featured product photo">'
     
	'</div>'
	);
# add the footer
footer.print_footer()
print('</div>');
print('</body>');
print('</html>');