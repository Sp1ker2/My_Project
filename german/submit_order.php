<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$servername = "localhost";
$username = "root";
$password = "bs";
$dbname = "shop";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $product = $conn->real_escape_string($_POST['product']);
    $quantity = intval($_POST['quantity']);
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    $phone = $conn->real_escape_string($_POST['phone']);
    $address = $conn->real_escape_string($_POST['address']);
    $cap_color = $conn->real_escape_string($_POST['cap_color']);

    $sql = "INSERT INTO orders (product, quantity, name, email, phone, address, cap_color)
            VALUES ('$product', $quantity, '$name', '$email', '$phone', '$address', '$cap_color')";

    if ($conn->query($sql) === TRUE) {
        header("Location: order_confirmation.html?order_id=" . $conn->insert_id);
        exit();
    } else {
        echo "Ошибка: " . $sql . "<br>" . $conn->error;
    }
} else {
    echo "Форма не была отправлена.";
}

$conn->close();
?>
