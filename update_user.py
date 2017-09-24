#!python

# import modules
import footer, nav, database_connection, edit_user, js_includes, css_includes

database_connection.cur.execute('SELECT * from users')
user_list = database_connection.cur.fetchall()

user_row = []

print("Content-type:text/html\r\n\r\n");
print('<html>');
print('<head>');
print('<meta charset="utf-8">');
print('<title>');
print('Cad Dealer - List of Users');
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
print('<h3 style="padding-left: 30px;"">List of Users</h3>');
# define message area
print('<div class = "message-div"></div>');
# users table
print(
	'<table class = "update-user-tb">'
	'<tr class = "update-user-tb-menu">'
    '<td class = "update-user-tb-rd">ID</td>'
	'<td class = "update-user-tb-rd">First Name</td>'
	'<td class = "update-user-tb-rd">Last Name</td>'
	'<td class = "update-user-tb-rd">Email</td>'
	'<td class = "update-user-tb-rd">Job Title</td>'
	'<td class = "update-user-tb-rd">Age</td>'
	'<td class = "update-user-tb-rd">Action</td>'
	'</tr>'
	);
if len(user_list) > 0:
	for user_row in user_list:
	    user_id = user_row[0]
	    first_name = user_row[1]
	    last_name = user_row[2]
	    email = user_row[3]
	    job_title = user_row[4]
	    age = user_row[5]
	    print(
		'<tr class = "update-user-tb-rw" id = "update-user-tb-rw_%d">'
	    '<td class = "update-user-tb-rd">%d</td>'
	    '<td class = "update-user-tb-rd">%s</td>'
	    '<td class = "update-user-tb-rd">%s</td>'
	    '<td class = "update-user-tb-rd">%s</td>' 
	    '<td class = "update-user-tb-rd">%s</td>'
        '<td class = "update-user-tb-rd">%d</td>'
	    '<td class = "update-user-tb-rd">'
	    '<button class = "btn btn-link" id = "edit-user-%d" data-toggle = "modal" data-target = "#%d">Edit</button>'
	    '<button value = "%d" class = "btn btn-link delete-user" id = "delete-user-%d">&times;</button>'
	    '</td>'
	    '</tr>' 
	    %(user_row[0],user_row[0],user_row[1],user_row[2],user_row[3],user_row[4],user_row[5],user_row[0],user_row[0],user_row[0],user_row[0])
		);
	    edit_user.edit_user_modal(user_id, first_name, last_name, email, job_title, age)
	    
else:
	print(
		'<tr class = "update-user-tb-rw">'
    	'<td>No user found</td>'
    	'</tr>'
		);
print('</table>');
print('</div>');
# end of form div
# add the footer
footer.print_footer()
print('</div>');
print('</body>');
print('</html>');
