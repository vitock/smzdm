
import hashlib
import base64
import os
import sys
from aes import AEScoder
import uuid
if __name__ == "__main__":
    env_dist = os.environ #
    # key =  env_dist["cookiekey"]
    print("您的cookie 加密密码:\n")
    key = str(uuid.uuid4());
    key=key.replace("-","",100);
    print(key);
    t = AEScoder(key);
    p = open("/".join([sys.path[0], "cookie.txt"])).read();
    e = t.encrypt(p);
    text_file = open("cookie.enc", "w")
    text_file.write(e);
    text_file.close()
    p2 = t.decrypt(e);
    print ("",p2 == p );

    