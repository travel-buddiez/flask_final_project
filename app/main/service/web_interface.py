# import uuid
# import datetime

# from .. import db
# from ..model.user import User

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from ..models import Profile

# import os


# def index(request):
#     return render(request, "travel_buddiez/homenlil.html")

# def login_goto(request):
#     return render(request, "travel_buddiez/login.html")

# def signup_goto(request):
#     return render(request, "travel_buddiez/signup.html")

# def loggin_landing_goto(request):
# #auth client side
#     return render(request, "travel_buddiez/homelil.html")

# def profile_view_goto(request):
#     usr = User.objects.get(id=id)
#     print(usr)
#     all_profile = Profile.objects.filter(username=request.user)
#     print(all_profile)
#     for prof in all_profile:
#         print(prof.firstname)
#         if prof.username == usr.username:
#             my_profile = prof
#             break
#     else:
#         print("Didn't Work")
#         my_profile = ""

#     context = {
#         "profile" : my_profile
#     }

#     print(my_profile)

#     return render(request, "travel_buddiez/profile_view.html", context=context)

# def continent_goto(request):
#     return render(request, "travel_buddiez/<continent:id>.html")

# def continent_detail_view_goto(request):
#     return render(request, "travel_buddiez/<continent:id>/<tcs:id>.html")




# # continents and
# # continent details




# #     usr = User.objects.get(id=id)
# #     print(usr)
# #     all_profile = Profile.objects.filter(username=request.user)
# #     print(all_profile)
# #     for prof in all_profile:
# #         print(prof.firstname)
# #         if prof.username == usr.username:
# #             my_profile = prof
# #             break
# #     else:
# #         print("Didn't Work")
# #         my_profile = ""

# #     context = {
# #         'profile' : my_profile
# #     }

# #     print(my_profile)

# #     return render(request, 'mealburner_app/profile_view.html', context=context)











# def save_new_user(data):
# email = User.query.filter_by(email=data['email']).first()
# username = User.query.filter_by(username=data['username']).first()
# print(data)
# if not email and not username:
#     if data['admin']:
#         print('admin')
#         new_user = User(
#             public_id=(str(uuid.uuid4())),
#             email=data['email'],
#             username=data['username'],
#             password=data['password'],
#             registered_on=datetime.datetime.utcnow(),
#             admin=data['admin']
#         )
#     else:
#         new_user = User(
#             public_id=(str(uuid.uuid4())),
#             email=data['email'],
#             username=data['username'],
#             password=data['password'],
#             registered_on=datetime.datetime.utcnow(),
#             admin=data['admin']
#         )

#     save_changes(new_user)
#     print('saved')
#     response_object = {
#         'status': 'success',
#         'message': 'Successfully registered.'
#     }
#     return generate_token(new_user)
# else:
#     response_object = {
#         'status': 'fail',
#         'message': 'User already exists. Please Log in.',
#     }
#     return response_object, 409


# def get_all_users():
# return User.query.all()


# def get_a_user(public_id):
# return User.query.filter_by(public_id=public_id).first()


# def save_changes(data):
# db.session.add(data)
# db.session.commit()


# def generate_token(user):
#     try:
#         auth_token = user.encode_auth_token(user.id)
#         response_object = {
#             'status': 'success',
#             'message': 'Successfully registered.',
#             'Authorization': auth_token.decode()
#         }
#         print('returning generate token')
#         return response_object, 201
#     except Exception as e:
#         response_object = {
#             'status': 'fail',
#             'message': 'Some error occurred. please try again'
#         }
#         return response_object, 401
