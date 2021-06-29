from graph_api_access import getCreds, doAPIcall
import datetime

def debugAccessToken( params ) :
	endpointParams = dict()
	endpointParams['input_token'] = params['access_token'] 
	endpointParams['access_token'] = params['access_token'] 
    
	url = params['graph_domain'] + '/debug_token' 

	return doAPIcall( url, endpointParams, params['debug'] ) 

params = getCreds() 
params['debug'] = 'yes' # set debug
response = debugAccessToken( params ) # hit the api for some data!

print ("\nData Access Expires at: ") 
print (datetime.datetime.fromtimestamp( response['json_data']['data']['data_access_expires_at'] )) # display out when the token expires

print ("\nToken Expires at: " )
print (datetime.datetime.fromtimestamp( response['json_data']['data']['expires_at'] )) # display out when the token expires