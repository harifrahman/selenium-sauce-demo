class DataProvider:

  login_data = [
  ('standard_user', 'wrong_pass', 'Epic sadface: Username and password do not match any user in this service'),
  ('wrong_username', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service'),
  ('standard_user', '', 'Epic sadface: Password is required'),
  ('', 'secret_sauce', 'Epic sadface: Username is required')
]