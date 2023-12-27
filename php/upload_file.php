<?php

$file = $_FILES["filename"]["name"];

move_uploaded_file($_FILES["filename"]["tmp_name"], "./uploads/" . $file);
echo $_SERVER['PHP_SELF'];

?>
