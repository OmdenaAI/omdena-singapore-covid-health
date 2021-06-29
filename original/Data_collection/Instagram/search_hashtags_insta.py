from graph_api_access import getCreds, doAPIcall
import sys
import json

def getHashtagInfo( params ) :
	""" API Endpoint:
		https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}
	"""
	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id'] 
	endpointParams['q'] = params['hashtag_name']
	endpointParams['fields'] = 'id,name'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + 'ig_hashtag_search'

	return doAPIcall( url, endpointParams, params['debug'] )

def getHashtagMedia( params ) :
	"""API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}
	"""
	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id']
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type']

	return doAPIcall( url, endpointParams, params['debug'] )


def writeInFile(data, file):
	datta = json.dumps(data, indent = 4)
	f = open(file, 'a')
	f.write(datta)



words = ['harassment', 'abuse', 'domestic', 'violence', 'beat', 'accused', 'woman', 'creep', 'molestation', 'shame', 'illegal', 'report', 'justice', 'lockdown', 'victim']

try : 
	fileName = sys.argv[1] # file to copy info to
except : # default to this file
	hashtag = 'bddjson.json'

for hashtag in words :
	params = getCreds() 
	params['hashtag_name'] = hashtag 
	hashtagInfoResponse = getHashtagInfo( params ) 
	params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; 
 
	print ("\nHashtag: " + hashtag) 
	
	params['type'] = 'top_media' # set call to get top media for hashtag
	hashtagTopMediaResponse = getHashtagMedia( params )

	writeInFile('[', fileName)
	
	for post in hashtagTopMediaResponse['json_data']['data'] : # loop over posts
		writeInFile(post, fileName)
		writeInFile(',', fileName)

	params['type'] = 'recent_media' # set call to get recent media for hashtag
	hashtagRecentMediaResponse = getHashtagMedia( params )

	for post in hashtagRecentMediaResponse['json_data']['data'] : # loop over posts
		writeInFile(post, fileName)
		writeInFile(',', fileName)

	writeInFile(']', fileName)



"""
	
	f = open("testyo.json", "a")
	f.write(hashtagTopMediaResponse['json_data']['data'])
	f.write(hashtagRecentMediaResponse['json_data']['data'])
"""

"""
words = ['harassment', 'abuse', 'domestic', 'violence', 'beat', 'accused', 'woman', 'creep', 'molestation', 'shame', 'illegal', 'report', 'justice', 'lockdown', 'victim']

for hashtag in words :
	params = getCreds() 
	params['hashtag_name'] = hashtag 
	params['debug'] = 'yes' 
	hashtagInfoResponse = getHashtagInfo( params ) 
	params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; 

	params['type'] = 'top_media' # set call to get top media for hashtag
	hashtagTopMediaResponse = getHashtagMedia( params )

	params['type'] = 'recent_media' # set call to get recent media for hashtag
	hashtagRecentMediaResponse = getHashtagMedia( params )	
"""


"""
try : 
	hashtag = sys.argv[1] # hashtag to get info on
except : # default to this hashtag
	hashtag = 'nope'
"""
"""
for hashtag in words :
	params = getCreds() 
	params['hashtag_name'] = hashtag 
	hashtagInfoResponse = getHashtagInfo( params ) 
	params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; 

	
	print ("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG INFO <<<<<<<<<<<<<<<<<<<<\n") 
	print ("\nHashtag: " + hashtag) 
	print ("Hashtag ID: " + params['hashtag_id']) 

	print ("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG TOP MEDIA <<<<<<<<<<<<<<<<<<<<\n") 
	params['type'] = 'top_media' # set call to get top media for hashtag
	hashtagTopMediaResponse = getHashtagMedia( params )

	for post in hashtagTopMediaResponse['json_data']['data'] : # loop over posts
		print ("\n\n---------- POST ----------\n") 
		print ("Link to post:") 
		print (post['permalink']) 
		print ("\nPost caption:")
		print (post['caption']) 
		print ("\nMedia type:") 
		print (post['media_type'])

	print ("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG RECENT MEDIA <<<<<<<<<<<<<<<<<<<<\n") 
	params['type'] = 'recent_media' # set call to get recent media for hashtag
	hashtagRecentMediaResponse = getHashtagMedia( params )

	for post in hashtagRecentMediaResponse['json_data']['data'] : # loop over posts
		print ("\n\n---------- POST ----------\n") 
		print ("Link to post:") 
		print (post['permalink'])
		print ("\nPost caption:")
		print (post['caption'])
		print ("\nMedia type:")
		print (post['media_type'])
	"""

