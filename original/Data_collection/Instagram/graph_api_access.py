import requests
import json



def getCreds():
    creds = dict()
    creds['access_token'] = 'EAAp48PZBZCqr4BAHl9ftBagOrQAz5CSVy8VKuAGlQg719NpcIL9Ap2qzebqvRknPH2Ws0dnjXt0g9OST8p9fDTKYhHhRbAZCMDqIikErAhegAxtonOSMevZCApNJPAifFiji7lkZBlFQzguQ5SNIxm49XjysMidUnVkujJTu8si1z1ZA1lbbm0'
    creds['client_id'] = '2947726245341886'
    creds['client_secret'] = '0adecbb6418d7fd4e0ebdd4520447b17'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v7.0'
    creds['endpoint_base'] =  creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = '106357124428037'
    creds['instagram_account_id'] = '17841436100657426'
    
    return creds

def doAPIcall(url, endPointParams, debug = 'no') :
    data = requests.get(url, endPointParams)
    
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endPointParams
    response['endpoint_params_pretty'] = json.dumps(endPointParams, indent = 4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent = 4)
    
    if ('yes' == debug) :
        displayApiCallData(response)
        
    return response

def displayApiCallData( response) : 
    print("\nURL: ")
    print(response['url']) 
    print("\nEndpoint Params: ") 
    print(response['endpoint_params_pretty']) 
    print("\nResponse: ") 
