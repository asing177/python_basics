import time, uuid
import urllib.request as urllib2
from urllib.parse import urlencode, quote_plus
import hmac, hashlib
from base64 import b64encode

"""
Basic info
"""
url = 'https://weather-ydn-yql.media.yahoo.com/forecastrss'
method = 'GET'
app_id = '3MXjoxHU'
consumer_key = 'dj0yJmk9dzlEWFAya0szeEJ1JmQ9WVdrOU0wMVlhbTk0U0ZVbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWJh'
consumer_secret = '78a8cb75835bf437ef763361cf745b20d3b7510b'
concat = '&'
query = {'location': 'sunnyvale,ca', 'format': 'json'}
oauth = {
    'oauth_consumer_key': consumer_key,
    'oauth_nonce': uuid.uuid4().hex,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': str(int(time.time())),
    'oauth_version': '1.0'
}

"""
Prepare signature string (merge all params and SORT them)
"""
merged_params = query.copy()
merged_params.update(oauth)
sorted_params = [k + '=' + urllib2.quote(merged_params[k], safe='') for k in sorted(merged_params.keys())]
signature_base_str =  method + concat + urllib2.quote(url, safe='') + concat + urllib2.quote(concat.join(sorted_params), safe='')


"""
Generate signature
"""
composite_key = urllib2.quote(consumer_secret, safe='') + concat
oauth_signature = b64encode(hmac.new(b'composite_key', b'signature_base_str', hashlib.sha1).digest())

"""
Prepare Authorization header
"""
oauth['oauth_signature'] = oauth_signature
auth_header = 'OAuth ' + ', '.join(['{}="{}"'.format(k,v) for k,v in oauth.items()])

"""
Send request
"""
url = url + '?' + urlencode(query, quote_via=quote_plus)
request = urllib2.Request(url)
request.add_header('Authorization', auth_header)
request.add_header('X-Yahoo-App-Id', app_id)
response = urllib2.urlopen(request).read()
