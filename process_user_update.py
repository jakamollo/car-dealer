#!python

# import modules
import footer, nav, database_connection, edit_user, js_includes, css_includes, cgi, cgitb
cgitb.enable()

# create an instance of FieldStorage
data = cgi.FieldStorage()

# check if form submission was made
email_exist_message = ''
if data['first_name']:
	# get form values
    first_name = data['first_name'].value
    last_name = data['last_name'].value
    email = data['email'].value
    job_title = data['job_title'].value
    age = data['age'].value
    user_unique_id = data['user_unique_id'].value
    	
    database_connection.cur.execute('UPDATE USERS set first_name = %s, last_name = %s, email = %s, job_title = %s, age = %s where id = %s' \
    ,(first_name, last_name, email, job_title, age, user_unique_id,))
    database_connection.conn.commit()
    
print("Content-type:text/html\n\n");
print(data);
