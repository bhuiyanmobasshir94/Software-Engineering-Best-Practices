from hashers import check_password, make_password

raw_password = "YOUR_RAW_PASS"


hashed_password = make_password(raw_password)

stored_hashed_password = hashed_password

login_password = "YOUR_LOGIN_PASS"

password_match = check_password(login_password, stored_hashed_password)

if password_match:
    print("Logged In!")
else:
    print("Password didn't match!")
