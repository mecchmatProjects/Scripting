#!venv/bin/python
import jwt
from itsdangerous import JSONWebSignatureSerializer

ALGO = "HS256"

class Signer:



    def __init__(self, secret: str, salt: str):
        self.__secret = secret
        self.__salt = salt

    def encode(self, data, out, way="jwt"):
        if not isinstance(data.list):
            raise ParseError("Hmm, what is it?")

        with open(out,"w") as f:

            for item in data[:HOW_MUCH]:
                try:
                    json.dump(f,self.encode(item))
                except ValueError as e:
                    raise e

    def decode(self, data, out, way="jwt"):
        if not isinstance(data.list):
            raise ParseError("Hmm, what is it?")

        with open(out, "w") as f:

            for item in data[:HOW_MUCH]:
                try:
                    json.dump(f, self.decode(item))
                except ValueError as e:
                    raise e

    def encode(self, data_dict:dict, way="jwt"):
        encoded = None
        if way=="jwt":
            encoded = jwt.encode(data_dict, self.__secret, algorithm=self.algo)

        elif way=="itsdangerous":
            s = JSONWebSignatureSerializer(self.__secret, salt=self.__salt, algorithm_name=self.algo)
            encoded = s.dumps(data_dict)


        return encoded

    def encode(self, data_str:str, way="jwt"):
        encoded = None
        if way=="jwt":
            encoded = jwt.encode(data_str, self.__secret, algorithm="HS256")

        elif way=="itsdangerous":
            s = JSONWebSignatureSerializer(self.__secret)
            encoded = s.dumps(data_str)
        else:
            raise LookupError("Who r u?")
        return encoded

    def encodeX(self, data_str, way="jwt"):

        if isinstance(data_str,str)  or isinstance(data_str,dict):
            return self.encode(data_str,way)
        raise

    def decode(self, encoded_string:str, way="jwt"):
        decoded = None
        if way == "jwt":
            decoded = jwt.decode(encoded_str, self.__secret, algorithm="HS256")

        elif way == "itsdangerous":
            s = JSONWebSignatureSerializer(self.__secret)
            decoded = s.dumps(data_str)

        return encoded







