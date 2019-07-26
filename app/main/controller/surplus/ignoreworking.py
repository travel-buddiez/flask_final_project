# from flask import Flask, jsonify

# app = travel_buddiez(__name__)

# users = {}
# user = {
#     username: input,
#     first_name: input,

# }

# @app.route('/', methods=['GET'])
# def home_nlil():
#     return render(request, travel_buddiez/nlil.html)
# #nlil=non-logged-in-landing

# def home_lil():
#     return render(request, travel_buddiez/lil.html)


# @app.route('/login', methods=['GET'])
# def login():
#     return f'<h1>hello {name}! Im using Flask</h1>'


# @app.route('/user_create', methods=['POST'])
# def create_user(data):
#     user = User.query.filter_by(username=data["username"]).first()
#     if user in usernames:
#         response_object = {
#             jsonify({
#                 "status": "fail",
#                 "message": "username already taken"
#                 })
#         }
#         return response_object, 409
#     else:
#         new_user = User(
#             id=str(uuid.uuid4()),
#             username=data["username"],
#             password=data["password"],
#             first_name=data["first_name"],
#             last_name=data["last_name"],
#             email=data["email"],
#             registered_on=datetime.datetime.utcnow()
#         )
#         save_changes(new_user)
#         response_object = {
#             jsonify({
#                 "status": "success",
#                 "message": "successfully registered"
#                 })
#         }
#         return response_object, 201


# def login_link



# import requests

# option = input("enter a choice: \n" \
#     "1. enter a name\n" \
#     "2. get names\n")

# if option == "1":
#     choice = input()
#     url = f"http://localhost:5000/home/{name}"
#     response = request.post(url)
#     if response.status_code == 200:
#         print("name save")
#     else:
#         print("something went wrong")
#     #elif "error" in response.json():
#         print(response.json()["error"])


# elif option == "2":
#     url == "http://localhost:5000/names/{name}"
#     response = requests.get(url).json()
#     print(response)
#     for name in response["names"]:
#         print(name)

# else:
#     print("no valid option detected")




