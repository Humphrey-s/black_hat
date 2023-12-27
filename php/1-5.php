<?php
$Today = date("l F d, Y");
?>
<html>
<head>
<title> Listing 1-5 </title>
</head>
<body>
Today's Date:
<?php

print("<H3>$Today</H3>\n");

print($_POST['YourName']);
print(", you will be out ");
print($_POST['CostOfLunch'] * $_POST['DayBuyingLunch']);
print(" dollars this week.<BR>\n");

?>
<p><?php

if (isset($UploadedFile))
{
	print("File present\n");
}
?></p>

<form action="upload_file.php"  method="post" enctype="multipart/form-data">
   <input type="file" name="filename">
   <input type="submit" value="upload">
</form>

</body>
</html>
