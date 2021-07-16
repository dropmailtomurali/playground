import os

from flask import Flask

app=Flask(__name__)

	
	
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Avatar</title>
<link href="css/style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="wrapper">
  <div id="banner">
    
  </div>
  <div class="menuBar">
    <ul>
      <li class="first"><a class="current">
	  
	  @app.route('/')
def sample_avatar():
	target = os.environ.get('TARGET', 'We are Team Avatar!')
	return 'Hello {}!\n'.format(target)
	
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
	  
	  
	  </a></li>
      
    </ul>
  </div>

  

</div>
</body>
</html>
