#!python

def edit_product(product_id,name,model,model_no,color,contacts,country_of_origin,distance_covered,engine_size,manufacturer,year,price,price_currency):
	
	print_edit_product = print(
		
		'<div class="modal fade modal-lg edit_product_modal" id="%d" data-backdrop="false" role="dialog">'
		# modal content
		'<div class="modal_content">'
		# modal header
		'<div class="modal_header">'
        '<h4 class="modal_header_title">Edit Product</h4>'
        '<button class="btn btn-sm edit-user-dismiss-btn" type="button" data-dismiss="modal">&times;</button>'
        '</div>'
        # modal body
        '<div class="modal_body" style = "margin-left:20px;">'
        # message div
        '<div id = "up_user_message_%d"></div>'
        '<form style = "margin-left:30px;" action="/cgi-bin/car_dealer/process_product_update.py" method="post" class = "new_product_form" enctype="multipart/form-data">'
        
        'Product Name: <input id = "pdct_name_%d" class = "pdct_name" value = "%s" style="margin-left:88px; margin-bottom:10px;margin-top:5px;" type="text" name="name" required/><br>'

        'Model: <input id = "pdct_model_%d" class = "pdct_model" value = "%s" style="margin-left:145px; margin-bottom:10px;" type="text" name="model" required/><br>'
        '<input id = "prdct_unq_id_%d" class = "up_pdct_unq_id" type="text" name = "product_id" value = "%d" hidden/>'

        'Model Number: <input id = "pdct_model_no_%d" class = "pdct_model_no" value = "%s" style="margin-left:83px; margin-bottom:10px;" type="text" name="model_no" required/><br>'

        'Color: <input id = "pdct_color_%d" class = "pdct_color" value = "%s" style="margin-left:150px; margin-bottom:10px;" type="text" name="color" required/><br>'

        'Contacts : <input id = "pdct_contacts_%d" class = "pdct_contacts" value = "%s" style="margin-left:125px; margin-bottom:10px;" type="text" name="contacts" required/><br>'

        'Country of Origin : <input id = "pdct_origin_%d" class = "pdct_origin" value = "%s" style="margin-left:65px; margin-bottom:10px;" type="text" name="country_of_origin" required/><br>'

        'Distance Covered : <input id = "pdct_dist_%d" class = "pdct_dist" value = "%d" style="margin-left:65px; margin-bottom:10px;" type="text" name="distance_covered" required/><br>'

        'Engine Size : <input id = "pdct_eng_sz_%d" class = "pdct_en_sz" value = "%s" style="margin-left:105px; margin-bottom:10px;" type="text" name="engine_size" required/><br>'

        'Manufacturer : <input id = "pdct_manuf_%d" class = "pdct_manuf" value = "%s" style="margin-left:90px; margin-bottom:10px;" type="text" name="manufacturer" required/><br>'

        'Year of Manufacture : <input id = "pdct_manuf_yr_%d" class = "pdct_manuf_yr" value = "%d" style="margin-left:47px; margin-bottom:10px;" type="text" name="year" required/><br>'

        'Price : <input id = "pdct_price_%d" class = "pdct_price" value = "%d" style="margin-left:155px; margin-bottom:10px;" type="text" name="price" required/><br>'

        'Price Currency : <input id = "pdct_price_curr_%d" class = "pdct_price_curr" value = "%s" style="margin-left:90px; margin-bottom:10px;" type="text" name="price_currency" required/><br>'

        'Product Photo : <input id = "pdct_photo_%d" class = "pdct_photo" class = "btn btn-primary" style="margin-left:87px; margin-bottom:10px;" type="file" name="photo" required/><br>'
        
        '<button value = "%d" class = "btn btn-primary update-product-submit-button" type="submit">Submit</button>'
        '</form>'

        '</div>'
        '</div>'
		'</div>'
		%(product_id,product_id,product_id,name,product_id,model,product_id,product_id,product_id,model_no,product_id,color,product_id,contacts,product_id,country_of_origin,product_id,distance_covered, \
			product_id,engine_size,product_id,manufacturer,product_id,year,product_id,price,product_id,price_currency,product_id,product_id)
		);

	return print_edit_product