# This example demonstrates showing some basic details about your lists
# Below you can see examples of pagination as well as partial response

from config import MailChimpConfig
import requests, json

config = MailChimpConfig()

endpoint = config.api_root + "/lists"
params   = {
    'fields': 'lists.id,lists.name,lists.stats.member_count', # With Partial Response, you choose which fields you want to see
    'count': 10, 'offset': 0                                  # Pagination in API v3.0 is always done with count and offset
}

total_lists = 0

while True:
    response = requests.get(endpoint, auth=('apikey', config.apikey), params=params, verify=False)
    body     = response.json()

    if (response.status_code != 200):
        print "Error: {} {}".format(str(response.status_code), response.reason)
        print json.dumps(response.json(), indent=4)
        break

    if len(body['lists']) == 0:
        break
    
    total_lists += len(body['lists'])

    for list in response.json()['lists']:
        print u'{}: {} (Subscribers: {})'.format(list['id'], list['name'], list['stats']['member_count'])
        
    params['offset'] += params['count']

print "\n" + str(total_lists) + " lists found."