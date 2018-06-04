<?php
header('X-XSS-Protection:0');
$name="";
$info="";
if(isset($_GET['name'])){
  $name = $_GET['name'];
  echo "<h2>Dear ".$_GET['name'].", Dhanyawaad aapka for Subscribing our Newsletter. ab aap iss parivar ke ek bahumulye sadasya hai!!</h2>";
}
if(isset($_GET['email'])){
  $email = $_GET['email'];
}
 ?>

<html>
<head>
  <title>XSS</title>
</head>
<body>
  <center>
    <h1>Newsletter Subscription</h1>
  <form method="get" action="index.php">
    Name:<input type="text" name="name"><br>
    Email:<input type="email" name="email"><br>
    <button type="submit">Submit</button>
  </form>
</center>
</body>
</html>
