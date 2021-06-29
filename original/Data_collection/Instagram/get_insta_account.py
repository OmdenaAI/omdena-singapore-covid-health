from graph_api_access import getCreds, doAPIcall

def getInstaAccount( params ) :
	""" 
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account
	"""

	endpointParams = dict()
	endpointParams['access_token'] = params['access_token'] 
	endpointParams['fields'] = 'instagram_business_account' 

	url = params['endpoint_base'] + params['page_id'] 

	return doAPIcall( url, endpointParams, params['debug'] ) # make the api call to endpoint url

params = getCreds() 
params['debug'] = 'no' # set debug
response = getInstaAccount( params ) 

print ("\n---- INSTAGRAM ACCOUNT INFO ----\n")
print ("Page Id:" )
print (response['json_data']['id'] )
print ("\nInstagram Business Account Id:" )
print (response['json_data']['instagram_business_account']['id'] )