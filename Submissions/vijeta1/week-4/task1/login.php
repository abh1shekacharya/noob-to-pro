<?php

$username=$_POST['username'];
$password=$_POST['password'];
$query="select username,pass from users where username='$username' and password='$password' limit 0,1";
$result=mysql_query($query);
$rows=mysql_fetch_array($result);
if($rows)
{
echo "Login Successful";
create_session();
}
else
{
echo "Username or Password is incorrect";
}
?>
