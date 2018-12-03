import base64
import hashlib
from time import gmtime, strftime


now = strftime("%m/%d/%Y %I:%M:%S %p", gmtime()) # Time now
ip = '127.0.0.1' # For example you can get user IP address by - request.META['REMOTE_ADDR']
password = 'defaultpassword' # Links re-publishing protection password in WMSPanel
validminutes = '60' # Token valid time

m = hashlib.md5()
m.update((str(ip) + str(password) + str(now) + str(validminutes)).encode('utf-8'))

base64hash = base64.b64encode(m.digest()).decode('utf-8')

urlsignature = (str('server_time=') + str(now) + str('&hash_value=') + str(base64hash)
+ str('&validminutes=') + str(validminutes)).encode("utf-8")

base64urlsignature = base64.b64encode(urlsignature).decode("utf-8")

print(base64urlsignature)
