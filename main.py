#!usr/bin/python
import webapp2
from google.appengine.ext import ndb
   
   
html = """ 
<html>
<head>
<title>
LIBRARY MANAGEMENT SYSTEM
</title>
<style>
h1{background-color:black;
color:white;
}
</style>
</head>
<body>
<center>
<h1>LIBRARY MANAGEMENT SYSTEM</h1></br></br>
<form action="/confirm" method="post">
<b>ENTER YOUR FULL NAME&nbsp;&nbsp;</b><input type="text" 

name="namec"></br></br>
<b>ENTER YOUR EMAIL&nbsp;&nbsp;</b> <input type="email" 

name="emailid"></br></br>
<b>ID&nbsp;&nbsp;</b><input type="text" name="id"></br></br> 
<b>NAME OF BOOK&nbsp;&nbsp;</b><input type="text" 

name="nameb"></br></br>
<b>INTERESTED GENRE&nbsp;&nbsp;</b><input type="text" 

name="ig"></br></br>

<input type="reset"> <input type="submit">
</center>
</form>
</body>
</html>
 """  
   
   
class library(ndb.Model):
     clientname = ndb.StringProperty(indexed=True)
     emailid = ndb.StringProperty(indexed=True)
     lid = ndb.StringProperty(indexed=True)
     bookname = ndb.StringProperty(indexed=True)
     interestedgenre = ndb.StringProperty(indexed=True)	 
     when = ndb.DateTimeProperty(auto_now_add=True)
	 
	 
	 
class MyHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html)
		
		
		
		
class MainHandler(webapp2.RequestHandler):
   def post(self):
     Clientname = self.request.get('namec')
     emailid = self.request.get('emailid')
     bookid = self.request.get('id')
     bookname = self.request.get('nameb')
     intgen = self.request.get('ig')
     lib= library()
     lib.clientname=Clientname
     lib.emailid=emailid
     lib.lid=bookid
     lib.bookname=bookname
     lib.interestedgenre=intgen
     lib.put()
     self.redirect('/')
	 
app = webapp2.WSGIApplication([('/', MyHandler),('/confirm', MainHandler), 
 debug=True)
