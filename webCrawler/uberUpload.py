# This is an example of file uploading using scrapy to a server that uses uberuploader.
# The spider logins to the page to make the upload, some webpages dont need to be logged in order to upload.
# IMPORTANT : You should increment DOWNLOAD_TIMEOUT in settings.py, but by the time this snippet was wrote isnt working fine. I recompile the whole scrapy changing the default of 3min. 
# Observations about my snippet:
# Is possible this is not the best code, please comment corrections.
# This could or should be implemented in a downloader middleware or pipeline?
# Don't show uploading state.
# Mime message creating could or should be in other place.
 
class fileUploadSpider(CrawlSpider):
   name = "spidertrigger.upload"
   allowed_domains = ["uploadhost.com"]
   start_urls = [
       "http://www.uploadhost.com/url_to_login_page",
   ]
 
   def parse(self,response):
	return [FormRequest.from_response(
			response,
			formdata={'user':'username','password':'secret'},
			callback=self.after_login,
		)]
 
   def after_login(self,response):
	if "Log in to your account" in response.body:
		self.log("Login Failed",level=log.ERROR)
		return
	else:
		dataObjetcs = DataObject.objects.all()#I am using django ORM
		for data in dataObjects:
                        #note the next line, the url should point to ubr_link_upload.php
                        # I will get the random ticket to be able to upload file,rnd_id is hardcoded but could be generated via code
			yield Request(
					url='http://upload.uploadhost.com/upload/ubr_link_upload.php?rnd_id=1280793046605',
					callback=self.obtener_id_upload,
					meta={'data' : data},
					)
	return
 
   def get_id_upload(self,response):
	#here I will get the upload id
        hxs = HtmlXPathSelector(response)
	data = response.request.meta['data']
	file_name = settings.IMAGES_STORE+'/'+data.path+'.zip' #here I require that the file exist (you should add more code here , like a try catch)
        #get the upload_id
	upload_id = re.search('\\\"\w+\\\"',hxs.select('/html/body').extract()[0]).group(0).replace('\"','')
 
        #build the fields that the request will have
	fields = {		'title':data.nombre,
				'adpaid' :'0',
				'private':'no',
				'category[]':'1',
				'fontcolor':'black',
				'helpbox' : 'Font size: [size=50%]small text[/size]',
				'textarea':'',
				'fontsize':'',
				'compare' : '14936',
				}
	files = {'upfile_0':file_name,}
	headers,body = self.get_mime(fields,files)	
	print 'Iniciando Request POST'
        #next NOTE that the url should point to cgi-bin/ubr_upload.pl with the proper upload_id
	yield FormRequest (
			url='http://upload.uploadhost.com/cgi-bin/ubr_upload.pl?upload_id='+upload_id,
			method='POST',
			body=body,
			meta={'data' : data},
			headers = headers,
			callback=self.lastcall,
		)
 
	return
 
   #this lastcall is for postprocessing the upload data, is an artificial example to obtain the id of the upload object on the webpage
   def lastcall(self,response):
 
	hxs = HtmlXPathSelector(response)
	linkUploaded = hxs.select('//div[@id=\'col2contentright\']/p/strong/a/@href').extract()[0]
	idUploaded = re.search('\d+',linkUploaded)
        print "Success Uploaded "+ ipUploaded
	return
 
   #this next code will need more improvement, is working for now. It could have problems with binary data!
   def get_mime(self,fields,files):
	BOUNDARY = '----------BOUNDARY_$'
#	CRLF = 
	L = StringIO()
	for key in fields.keys() :
		value = fields[key]
		L.write('--' + BOUNDARY+'
')
		L.write('Content-Disposition: form-data; name="%s"' % key+'
')
		L.write(''+'
')
		L.write(value.encode('utf-8')+'
')
    	for key in files.keys():
		value = files[key]
		filename = value
		L.write('--' + BOUNDARY+'
')
		L.write('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, 'full.zip')+'
')
		L.write('Content-Type: %s' % self.get_content_type(filename)+'
')
		L.write(''+'
')
		L.write(open(value,'rb').read()+'
')
	L.write('--' + BOUNDARY + '--'+'
')
	L.write(''+'
')
 
	body = L.getvalue()
 
	content_type = {'Content-Type': 'multipart/form-data; boundary=%s' % BOUNDARY }
	return content_type,body
 
   def get_content_type(self,filename):
	return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
 
# Snippet imported from snippets.scrapy.org (which no longer works)
# author: llazzaro
# date  : Aug 15, 2010
 
