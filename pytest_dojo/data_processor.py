def get_user_by_id(user_list, user_id):
    for user in user_list:
        if user['id'] == user_id:
            return True
    return None

def get_admin_emails(user_list):
    return [user['email'] for user in user_list if user['role'] == 'admin'] 