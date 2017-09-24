#!python

# import modules here
import cgi, cgitb, database_connection, footer, nav, js_includes, css_includes
cgitb.enable()


# create an instance of FieldStorage
form = cgi.FieldStorage()
# check if form submission was made
email_exist_message = ''
if form.getvalue('first_name'):
    # get form values
    first_name = form.getvalue('first_name')
    last_name = form.getvalue('last_name')
    email = form.getvalue('email')
    job_title = form.getvalue('job_title')
    age = form.getvalue('age')

    # Check if the email address already exist in the database
    database_connection.cur.execute('SELECT email from users where email = %s',(email,))
    email_list = database_connection.cur.fetchone()
    if email_list == None:
        # insert the user info to the database
        database_connection.cur.execute('INSERT INTO users(first_name, last_name, email, job_title, age) \
        VALUES (%s, %s, %s, %s, %s)',(first_name, last_name, email, job_title, age))

        # commit and close transaction and connection
        database_connection.conn.commit()
        database_connection.conn.close()
    else:
    	email_exist_message = 'The email %s' % email_list + ' already exist. Please try another one.'
 	
print("Content-type:text/html\n\n");
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
if email_exist_message != '':
	print('<p class = "email-exist-para" style ="padding-left:5px;padding-top:5px;height:30px;width:420px;border:5px;margin-left:15px;background-color:lightpink;">' + email_exist_message + '</p>');
print('<form action="/cgi-bin/car_dealer/process_new_user.py" method="post" class = "new_user_form">');
print('First Name: <input style="margin-left:10px; margin-bottom:10px;" type="text" name="first_name"/><br>');

print('Last Name: <input style="margin-left:10px; margin-bottom:10px;" type="text" name="last_name"/><br>');

print('Email: <input style="margin-left:42px; margin-bottom:10px;" type="text" name="email"/><br>');
print("\n");

print('Job Title: <input style="margin-left:25px; margin-bottom:10px;" type="text" name="job_title"/><br>');

print('Age : <input style="margin-left:47px; margin-bottom:10px;" type="text" name="age"/><br>');
print('<button type="submit" classs = "new-user-submit-button">Submit Button</button>');
print('</form>');
print('</div>');
# end of form div
# add the footer
footer.print_footer()
print('</div>');
print('</body>');
# include js files here

print('</html>');
