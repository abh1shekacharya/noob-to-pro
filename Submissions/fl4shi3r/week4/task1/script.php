<?php
$username = $_POST['input_username'];
$password = $_POST['input_password'];

mysql_connect('localhost',"root","");
mysql_select_db("login");

$result= mysql_query("SELECT * FROM users where username = '$username' and password = '$password'") or die("Failed to query",mysql_error());
$row= mysql_array ($result);
if ($row['username']==$username && $row['password']==$password) {
	echo "Login Succeeded";
}
else {
echo "Login Failed";
}
?>
