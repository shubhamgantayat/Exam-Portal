from werkzeug.security import check_password_hash
import config


class Validation:

    def __init__(self, email, password):
        try:
            self.email = email
            self.password = password
        except Exception as e:
            config.logger.log("ERROR", str(e))

    def check(self):
        """

        :return: whether valid or not along with a new jwt.
        """
        try:
            if self.email is not None and self.password is not None:
                self.email = self.email.lower()
                result = config.mongo_db.my_db['User'].find({"email": self.email})[0]
                if result is None:
                    config.logger.log("CRITICAL", "Invalid Credentials")
                    return {"role": False, "message": "Invalid Credentials", "token": None}
                else:
                    if check_password_hash(result['password'], self.password):
                        config.logger.log("INFO", "Login successful...")
                        return {"result": result, "message": "Login successful"}
                    else:
                        config.logger.log("WARNING", "Wrong password...")
                        return {"role": False, "message": "Wrong password"}
            else:
                return {"role": False, "message": "Please enter an email and password to log in"}
        except Exception as e:
            config.logger.log("ERROR", str(e))
            return {"role": False, "message": "Internal Server Error"}
