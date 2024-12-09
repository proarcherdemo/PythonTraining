
from dao.logindao import LoginDAO 
class LoginBL:
    def getLoginDetailsBL(username, password):
        print("Into Login BL. Invoking DB to get the user details")
        return LoginDAO.getLoginDeatilsFromDB(username, password)