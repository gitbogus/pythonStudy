# Python 샘플 코드 #
# try:
#     from urllib.request import urlopen
# except ImportError:
#     from urllib2 import urlopen

from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus


skey = 'Al5dwUCfM5vQOBl8Lx7R8Jl4Wr5T0jFyWCaGZ7vxjE4s4svNU%2FZU1DFJQLS%2Fya%2F7S6I1xoYUr%2Fnl%2FYrCFczpLg%3D%3D'
url = 'https://infuser.odcloud.kr/oas/docs?namespace=15077603/v1'
params = '?' + 'ServiceKey=' + skey + '&' + \
urlencode({ quote_plus('pageNo') : '1', 
quote_plus('perPage') : '10', quote_plus('returnType') : 'Json', 


print(url+params)

# request = Request(url + params)
# request.get_method = lambda: 'GET'
# response_body = urlopen(request).read()
# print(response_body)

# content = requests.get(url).content
# # dict = xmltodict.parse(content)
# print(content)