
import requests
import json

api_key = '9c15ddbbf054044978b1a395919c8ed4d74a9271f39b0250ac1a969e7698632c'
url = 'https://www.virustotal.com/api/v3/search?query='
header={'x-apikey': api_key}

# open files
mdf_hashes = open('mdf.txt')
output = open('details.csv','w')

# write header of the output file
output.write("md5,type_description,vhash,creation_date,last_modification_date,type_tag,size")

for mdf in mdf_hashes:
    response = requests.get(url+mdf,headers=header)
    response_json = json.loads(response.content)
    if response.status_code == 200 and not len(response_json['data']) == 0:
        type_description = response_json['data'][0]['attributes']['type_description']
        vhash = str(response_json['data'][0]['attributes']['vhash'])
        creation_date =  str(response_json['data'][0]['attributes']['creation_date'])
        last_modification_date = str(response_json['data'][0]['attributes']['last_modification_date'])
        type_tag = str(response_json['data'][0]['attributes']['type_tag'])
        size = str(response_json['data'][0]['attributes']['size'])
        output.write("\n"+mdf.strip()+","+type_description+","+vhash+","+creation_date+","+last_modification_date+","+type_tag+","+size)
mdf_hashes.close()
output.close()


