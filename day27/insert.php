<?php
$name = $_REQUEST['name'];
$mail = $_REQUEST['mail'];
$passw = $_REQUEST['password'];
$conpass = $_REQUEST['confirmpass'];


$conn = mysqli_connect("localhost", "root", "", "phpcurd");


if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


$query = "INSERT INTO users (name, mail, password) 
          VALUES ('$name', '$mail', '$passw')";

$insert = mysqli_query($conn, $query);

if ($insert) {
    echo "<script>alert('DATA INSERTED');</script>";
} else {
    echo "<script>alert('DATA NOT INSERTED');</script>";
}

mysqli_close($conn);
?>