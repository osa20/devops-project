import pymysql
import requests
import time

time.sleep(180)


def backend_testings_func(user_id, user_name, creation_date):
    global user_data
    url = f"http://192.168.52.77:5000/users/{user_id}"

    # Postimg a new user data to the REST API using POST method
    try:
        post_request = requests.post(url, json={"user_name": user_name, "creation_date": creation_date})
        if post_request.ok:
            print(post_request.json())
        else:
            post_res_dict = post_request.json()
            print("error: cannot post new request,", post_res_dict['reason'] + str(','),
                  "status code:", post_request.status_code)

    except requests.exceptions.ConnectionError as reqExecConErr:
        print(reqExecConErr, "\n\nEnsure rest_app.py is running")
    print()

    # Submitting a GET request to make sure status code is 200
    # and data equals the posted data
    try:
        get_request = requests.get(url)
        if get_request.ok:
            get_response_user_name = get_request.json()['user_name']
            if get_response_user_name == user_name and get_request.status_code == 200:
                print("works correctly as expected,", get_response_user_name, "equal to:", user_name,
                      "\nstatus code is: ", get_request.status_code)
            else:
                print("Error:", get_response_user_name, "is not equal to posted user name:", user_name)
        else:
            get_res_dict = get_request.json()
            print(f"error: cannot retrieve get request, user:{user_id} does not exist",
                  get_res_dict['reason'] + str(','),
                  "status code:", get_request.status_code)

    except requests.exceptions.ConnectionError as reqExecConErr:
        print(reqExecConErr, "\n\nEnsure rest_app.py is running")
    print()

    # Checking that posted data was stored inside database (users table)
    schema_name = "mydb"
    # Establishing a connection to DB
    conn = pymysql.connect(host='172.17.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id={user_id}")

    # As there is just one user record...
    for row in cursor:
        user_data = row

    try:
        db_user_id = user_data[0]
        db_user_name = user_data[1]

        if db_user_name == user_name and db_user_id == user_id:
            print(f"{user_name} is stored in the right place, under id {user_id}"
                  "\ndb user_id:", db_user_id, "\ndb_user_name:", db_user_name)

    except UnboundLocalError as err:
        print(f"\n{user_name} is NOT stored in the right place")
        print("Error:", err)


# # For carrying out the backend testing
if __name__ == '__main__':
    backend_testings_func(14, "Timothy", "2023-08-31")
