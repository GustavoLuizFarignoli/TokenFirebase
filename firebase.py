#importar o pyrebase4 no pip
import pyrebase
from getpass import getpass


firebaseConfig = {
    "apiKey": "AIzaSyC4pVv2hJpN54ND5GOCcUgB6K4NmZN9R0M",
    "authDomain": "api-teste-266f1.firebaseapp.com",
    "projectId": "api-teste-266f1",
    "databaseURL": "https://" + "<ID_APP>" + ".firebaseio.com",
    "storageBucket": "api-teste-266f1.appspot.com",
    "messagingSenderId": "2457462666",
    "appId": "1:2457462666:web:b16f7f88a95dfb5121ca73",
    "measurementId": "G-40PE2RD42N"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.sign_in_with_email_and_password(user,password)
print("Resultado: ", status)



