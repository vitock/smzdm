
import hashlib
import base64
import os
import sys
from aes import AEScoder
import uuid
if __name__ == "__main__":
    env_dist = os.environ #
    print("您的cookie 加密密码:\n")
    if 'COOKIEENCKEY' in env_dist:
        key = env_dist['COOKIEENCKEY']
    else:
        # key =  env_dist["cookiekey"]
        
        key = str(uuid.uuid4());
        key=key.replace("-","",100);

    
    print(key);
    t = AEScoder(key);
    p = open("/".join([sys.path[0], "config.json"])).read();
    e = t.encrypt(p);
    text_file = open("config.json.enc", "w")
    text_file.write(e);
    text_file.close()
    p2 = t.decrypt(e);
    print ("",p2 == p );

    