#!python

# import modules

def edit_user_modal(user_id, first_name, last_name, email, job_title, age):
        
        print_user_edditing = print(
                '<div class="modal fade modal-lg edit_user_modal" id="%d" data-backdrop="false" role="dialog">'
		# modal content
		'<div class="modal_content">'
		# modal header
		'<div class="modal_header">'
                '<h4 class="modal_header_title">Edit User</h4>'
                '<button class="btn btn-sm edit-user-dismiss-btn" type="button" data-dismiss="modal">&times;</button>'
                '</div>'
                # modal body
                '<div class="modal_body" style = "margin-left:20px;">'
                # message div
                '<div id = "up_user_message_%d"></div>'
                '<form style = "margin-left:30px;" action="/cgi-bin/car_dealer/process_user_update.py" method="post" class = "edit_user_form">'
                'First Name: <input id = "up_user_fn_%d" class = "up_user_fn" value = "%s" style="margin-left:10px; margin-bottom:10px;" type="text" name="first_name"/><br>'
                'Last Name: <input id = "up_user_ln_%d" class = "up_user_ln" value = "%s" style="margin-left:10px; margin-bottom:10px;" type="text" name="last_name"/><br>'
                'Email: <input id = "up_user_eml_%d" class = "up_user_eml" value = "%s" style="margin-left:42px; margin-bottom:10px;" type="text" name="email"/><br>'
                '<input id = "up_user_unq_id_%d" class = "up_user_unq_id" type="text" name = "user_unique_id" value = "%d" hidden/>'
                'Job Title: <input id = "up_user_jt_%d" class = "up_user_jt" value = "%s" style="margin-left:25px; margin-bottom:10px;" type="text" name="job_title"/><br>'
                'Age : <input id = "up_user_age_%d" class = "up_user_age" value = "%d" style="margin-left:47px; margin-bottom:10px;" type="text" name="age"/><br>'
                '<button value = "%d" class = "btn btn-primary update-user-submit-button" type="submit">Submit</button>'
                '</form>'

                '</div>'
                '</div>'
		'</div>'
		% (user_id, user_id, user_id, first_name, user_id, last_name, user_id, email, user_id, user_id, user_id, job_title, user_id, age, user_id)
                );
        return print_user_edditing
	

	
