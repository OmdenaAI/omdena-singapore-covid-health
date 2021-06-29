from graph_api_access import getCreds, doAPIcall

def getLongTimeToken( params ) :
	endpointParams = dict()
	endpointParams['grant_type'] = 'fb_exchange_token' 
	endpointParams['client_id'] = params['client_id']
	endpointParams['client_secret'] = params['client_secret'] 
	endpointParams['fb_exchange_token'] = params['access_token']
	url = params['endpoint_base'] + 'oauth/access_token' 

	return doAPIcall( url, endpointParams, params['debug'] )

params = getCreds() 
params['debug'] = 'yes' 
response = getLongTimeToken( params ) 

print ("\n ---- ACCESS TOKEN INFO ----\n") 
print ("Access Token:")  
print (response['json_data']['access_token'])