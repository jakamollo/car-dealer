#!python

def edit_user_modal(user_id):
	
	print_user_edit_modal = print(
		'<div class="modal fade modal-lg subject_modal" id="%d" data-backdrop="false" role="dialog">'
		# modal content
		'<div class="modal_content">'
        
        '</div>'
		'</div>'
		% (user_id)
		);

	return print_user_edit_modal