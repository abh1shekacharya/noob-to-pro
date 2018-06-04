<?php
  $username = $_POST['user'];
  $password = $_POST['pass'];

  $dblink = mysqli_connect("localhost", "root", "");
  mysqli_select_db($dblink, "noob");
  // $mysqli = new mysqli("localhost", "root", "", "noob")

  $result = mysqli_query($dblink, "SELECT * FROM pro WHERE username = '$username' AND password = '$password'")
        or die("Database Kaha Hai!!".mysqli_error($dblink));
  $row = mysqli_fetch_array($result);
  if($row){
    echo "<h3>Padhariye \"".$username."\"</h3>";
    echo "<h2>PHP Sucks!!</h2>";
  }
  else {
    echo "<h2>Yeh Password Galat hai, Kripya Sahi password daale!!</h2>";
  }
?>
