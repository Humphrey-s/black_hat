<!DOCTYPE html>
<html>
<head>
<title> Hello World </title>
</head>
<body>
<p><?php

print ("hello world\n"); 

if (!isset( $_SERVER['HTTP_USER_AGENT']))
{
	print ("You are at home\n");
}
else
{
	print ($HTTP_USER_AGENT);
	print("\n");
}
?></p>
</body>
</html>
