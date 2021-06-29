from graph_api_access import getCreds, doAPIcall

def getPages( params ) :
	""" 
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}
	"""

	endpointParams = dict() 
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + 'me/accounts' 

	return doAPIcall( url, endpointParams, params['debug'] ) # make the api call to endpoint url

params = getCreds() 
params['debug'] = 'no' #switch to yes to have full response 
response = getPages( params ) 

print ("\n---- FACEBOOK PAGE INFO ----\n") 
print ("Page Name:") 
print (response['json_data']['data'][0]['name']) 
print ("\nPage Category:")
print (response['json_data']['data'][0]['category']) 
print ("\nPage Id:") 
print (response['json_data']['data'][0]['id'])