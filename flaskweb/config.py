import os
class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True

    #####need to add EMAIL_USER and EMAIL_PASS to win system environment variables to get it working####
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

##(tried to see if i get envs right##
#print (os.environ.get("EMAIL_USER"))
#print (os.environ.get("EMAIL_PASS"))
