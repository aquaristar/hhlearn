# response when new user is register and logged in
def response_user_registered_login_successful():
    response = dict()
    response['code'] = 'response_login_successful'
    response['status'] = 'success'
    response['message'] = 'User registered and login Successful.'
    response['detail'] = 'User registered and login Successful.'
    return response

# response when new user is registered
def response_signup_successful():
    response = dict()
    response['code'] = 'response_user_registered_successful'
    response['status'] = 'success'
    response['message'] = 'Signup Successful.'
    response['detail'] = 'Signup Successful.'
    return response

# response for login successful
def response_login_successful():
    response = dict()
    response['code'] = 'response_login_successful'
    response['status'] = 'success'
    response['message'] = 'Login Successful.'
    response['detail'] = 'Login Successful.'
    return response

# response for any any missing required fields.
def response_missing_fields():
    response = dict()
    response['code'] = 'response_missing_fields'
    response['status'] = 'error'
    response['message'] = 'Please fill all the required fields.'
    response['detail'] = 'Please fill all the required fields.'
    return response

# response for any any missing required fields.
def response_monthly_safety_1_0():
    response = dict()
    response['code'] = 'response_monthly_safety_1_0'
    response['status'] = 'error'
    response['message'] = 'Monthly safety values can only be 1 or 0'
    response['detail'] = 'Monthly safety values can only be 1 or 0'
    return response

# response for any any missing required fields.
def response_account_not_active():
    response = dict()
    response['code'] = 'response_account_not_active'
    response['status'] = 'error'
    response['message'] = 'Your account is not activated.'
    response['detail'] = 'Your account is not activated.'
    return response

# when user authentication is failed.
def response_authentication_failed():
    response = dict()
    response['code'] = 'response_authentication_failed'
    response['status'] = 'error'
    response['message'] = 'Authentication Failed.'
    response['detail'] = 'Authentication Failed.'
    return response

# when system is unable to add new user.
def response_unable_to_add_new_user():
    response = dict()
    response['code'] = 'response_unable_to_add_new_user'
    response['status'] = 'error'
    response['message'] = 'Unable to register new user. Please try again.'
    response['detail'] = 'Unable to register new user. Please try again.'
    return response

# when we are unable to get account details form kazoo server.
def response_unable_to_get_account_details_from_kazoo():
    response = dict()
    response['code'] = 'response_unable_to_get_account_details_from_kazoo'
    response['status'] = 'error'
    response['message'] = 'Unable to your account details. Please try again.'
    response['detail'] = 'Unable to your account details. Please try again.'
    return response

# when we are unable to get account details form kazoo server.
def response_email_not_valid():
    response = dict()
    response['code'] = 'response_email_not_valid'
    response['status'] = 'error'
    response['message'] = 'Please use a valid email address.'
    response['detail'] = 'Please use a valid email address.'
    return response

# when we are unable to get account details form kazoo server.
def response_username_already_used():
    response = dict()
    response['code'] = 'response_username_already_used'
    response['status'] = 'error'
    response['message'] = 'Username already used. Please use a different username.'
    response['detail'] = 'Username already used. Please use a different username.'
    return response

# when we are unable to find username in database.
def response_username_do_not_exist():
    response = dict()
    response['code'] = 'response_username_do_not_exist'
    response['status'] = 'error'
    response['message'] = 'Unable to find username.'
    response['detail'] = 'Unable to find username.'
    return response

# when we are unable to find username in database.
def response_password_reset():
    response = dict()
    response['code'] = 'response_password_reset'
    response['status'] = 'success'
    response['message'] = 'Please check your email for password reset email.'
    response['detail'] = 'Please check your email for password reset email.'
    return response

# when we are unable to find username in database.
def response_account_no_activated():
    response = dict()
    response['code'] = 'response_account_no_activated'
    response['status'] = 'error'
    response['message'] = 'Your account not activated. Please verify your account first.'
    response['detail'] = 'Your account not activated. Please verify your account first.'
    return response

# when we are unable to find username in database.
def response_passwords_not_same():
    response = dict()
    response['code'] = 'response_passwords_not_same'
    response['status'] = 'error'
    response['message'] = 'Passwords does not match.'
    response['detail'] = 'Passwords does not match.'
    return response

# when we are unable to find username in database.
def response_password_token_invalid():
    response = dict()
    response['code'] = 'response_password_token_invalid'
    response['status'] = 'error'
    response['message'] = 'Invalid Password Reset Token'
    response['detail'] = 'Invalid Password Reset Token'
    return response

# when we are unable to find username in database.
def response_password_updated():
    response = dict()
    response['code'] = 'response_password_updated'
    response['status'] = 'success'
    response['message'] = 'Your password is now updated.'
    response['detail'] = 'Your password is now updated.'
    return response

# when we are unable to find username in database.
def response_profile_save_successful():
    response = dict()
    response['code'] = 'response_profile_save_successful'
    response['status'] = 'success'
    response['message'] = 'Profile Updated'
    response['detail'] = 'Profile Updated'
    return response

# when we are unable to find username in database.
def response_course_type_missing():
    response = dict()
    response['code'] = 'response_course_type_missing'
    response['status'] = 'error'
    response['message'] = 'Course Type Missing'
    response['detail'] = 'Course Type Missing'
    return response

# when we are unable to find username in database.
def response_course_not_assigned():
    response = dict()
    response['code'] = 'response_course_not_assigned'
    response['status'] = 'error'
    response['message'] = 'This course is not assigned to you.'
    response['detail'] = 'This course is not assigned to you.'
    return response


# when we are unable to find username in database.
def response_course_started():
    response = dict()
    response['code'] = 'response_course_started'
    response['status'] = 'success'
    response['message'] = 'Course Started.'
    response['detail'] = 'Course Started.'
    return response

#response when test started
def response_test_started():
    response = dict()
    response['code'] = 'response_test_started'
    response['status'] = 'success'
    response['message'] = 'Test Started.'
    response['detail'] = 'Test Started.'
    return response

#response when test resumed
def response_test_resumed():
    response = dict()
    response['code'] = 'response_test_resumed'
    response['status'] = 'success'
    response['message'] = 'Test Resumed.'
    response['detail'] = 'Test Resumed.'
    return response

#response when test resumed
def response_test_exist():
    response = dict()
    response['code'] = 'response_test_exist'
    response['status'] = 'error'
    response['message'] = 'You have already taken test for this course'
    response['detail'] = 'You have already taken test for this course'
    return response

#response when test resumed
def response_test_dealyed():
    response = dict()
    response['code'] = 'response_test_delayed'
    response['status'] = 'error'
    response['message'] = 'You can not retake this test within 24 hrs.'
    response['detail'] = 'You can not retake this test within 24 hrs.'
    return response

# when we are unable to find username in database.
def response_group_update_failed():
    response = dict()
    response['code'] = 'response_group_update_failed'
    response['status'] = 'error'
    response['message'] = 'Group Update Failed'
    response['detail'] = 'Group Update Failed'
    return response

# when we are unable to find username in database.
def response_group_add_successful():
    response = dict()
    response['code'] = 'response_group_add_successful'
    response['status'] = 'success'
    response['message'] = 'New group added successfully'
    response['detail'] = 'New group added successfully'
    return response

# when we are unable to find username in database.
def response_group_update_successful():
    response = dict()
    response['code'] = 'response_group_update_successful'
    response['status'] = 'success'
    response['message'] = 'Group updated successfully'
    response['detail'] = 'Group updated successfully'
    return response

# when we are unable to find username in database.
def response_group_add_failed():
    response = dict()
    response['code'] = 'response_group_add_failed'
    response['status'] = 'error'
    response['message'] = 'Group addition failed, please try again.'
    response['detail'] = 'Group addition failed, please try again.'
    return response

# when we are unable to get account details form kazoo server.
def response_email_already_used():
    response = dict()
    response['code'] = 'response_email_already_used'
    response['status'] = 'error'
    response['message'] = 'Email already used. Please use a different email.'
    response['detail'] = 'Email already used. Please use a different email.'
    return response
