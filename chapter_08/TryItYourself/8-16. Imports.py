# import imports_module
# user_profile = imports_module.build_profile('albert','einstein', location = 'princeton', field = 'physics')
# print(user_profile)

# from imports_module import build_profile
# user_profile = build_profile('albert','einstein', location = 'princeton', field = 'physics')
# print(user_profile)

# from imports_module import build_profile as bp
# user_profile = bp('albert','einstein', location = 'princeton', field = 'physics')
# print(user_profile)

# import imports_module as im
# user_profile = im.build_profile('albert','einstein', location = 'princeton', field = 'physics')
# print(user_profile)

from imports_module import *
user_profile = build_profile('albert','einstein', location = 'princeton', field = 'physics')
print(user_profile)
