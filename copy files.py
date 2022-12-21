import shutil
import os
import stat

source = "/E:/assets/Badminton.gif"
destination = "/E:/test"
os.chmod(source, stat.S_IRWXG)

shutil.copy(source,destination )

