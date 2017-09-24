#!python

# import modules
import footer, nav, js_includes, css_includes
 	
print("Content-type:text/html\r\n\r\n");
print('<html>');
print('<head>');
print('<meta charset="utf-8">');
print('<title>');
print('Cad Dealer - New User');
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
print('<div class = "new-user-form-div">');
print('<h3 style="padding-left: 30px;"">Add New User</h3>');
# define message area
print('<div class = "message-div"></div>');
print('<form action="/cgi-bin/car_dealer/process_new_user.py" method="post" class = "new_user_form">');
print('First Name: <input style="margin-left:10px; margin-bottom:10px;" type="text" name="first_name"/><br>');

print('Last Name: <input style="margin-left:10px; margin-bottom:10px;" type="text" name="last_name"/><br>');

print('Email: <input style="margin-left:42px; margin-bottom:10px;" type="text" name="email"/><br>');
print("\n");

print('Job Title: <input style="margin-left:25px; margin-bottom:10px;" type="text" name="job_title"/><br>');

print('Age : <input style="margin-left:47px; margin-bottom:10px;" type="text" name="age"/><br>');
print('<button class = "new-user-submit-button" type="submit">Submit Button</button>');
print('</form>');
print('</div>');
# end of form div
# add the footer
footer.print_footer()
print('</div>');
print('</body>');
print('</html>');
