#!venv/bin/python
import argparse

import json

import signers

ALGO = "HS256"
HOW_MUCH = 5

"""
+ обязательный аргумент secret: str
+ обязательный аргумент salt: str
+ обязательный аргумент action = encode/decode
+ обязательный аргумент using = pyjwt/itsdangerous
+ необязательный аргумент expiration = N seconds 
+ обязательный аргумент input = *.json файл  
+ обязательный аргумент output = *.json файл  
"""
parser = argparse.ArgumentParser(description="signer")
parser.add_argument("-s", "--secret", type="str", help="Secret key", required=True)
parser.add_argument("-st", "--salt",type="str", help="Secret salt", required=True)
parser.add_argument("-a", "--action",type="str", choices=["encode","decode"], help="encode/decode", required=True)
parser.add_argument("-u", "--using", type="str", choices=["pyjwt","itsdangerous"], help="pyjwt/itsdangerous", required=True)
parser.add_argument("-e", "--expiration", type="int", help="N seconds", required=False)
parser.add_argument("-i", "--input", help="input json", required=True)
parser.add_argument("-o", "--output", help="output json", required=True)
args = parser.parse_args()

if __name__ == "__main__":

    print("Args is -> {args}".format(args=args))

    sign = Signer(args.secret, args.salt)
    sign.algo = ALGO
    sign.use = args.using
    sign.how_much = HOW_MUCH

    sign.expir = args.expiration

    with open(args.input) as f:
        d = json.load(f)
        print(d)

        try:
            if args.action == "encode":
                sign.encode(d,args.output)
            else:
                sign.decode(d, args.output)
        except ParseError as e:
            print(e)
        except ValueError as e:
            print(e)
        except LookupError as e:
            print(e)







