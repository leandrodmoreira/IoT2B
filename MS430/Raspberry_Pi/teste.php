<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<body>

Teste de HTML1

<?php

echo "Teste HTML 1.5";

$hostname = "192.168.0.38";
$username = "root";
$password = "@cthum@1979";
$db = "iot2b";

echo "$hostname";
echo "$username";
echo "$password";
echo "$db;

$dbconnect=mysqli_connect($hostname,$username,$password,$db);

echo "$username";

echo "$dbconnect";

if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}

?>
Teste de HTML2
<table border="1" align="center">
<tr>
  <td>id</td>
</tr>

<?php

$query = mysqli_query($dbconnect, "SELECT * FROM airData")
   or die (mysqli_error($dbconnect));

while ($row = mysqli_fetch_array($query)) {
  echo
   "<tr>
    <td>{$row['id']}</td>
   </tr>\n";

}

?>
Teste de HTML 3
</table>
</body>
</html>