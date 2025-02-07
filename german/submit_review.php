<?php
$host = 'localhost';
$dbname = 'comments_db';
$username = 'root';
$password = 'bs';

$conn = new mysqli($host, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Ошибка подключения: " . $conn->connect_error);
}

$product_id = $_POST['product_id'];
$user_name = $_POST['user_name'];
$rating = $_POST['rating'];
$comment = $_POST['comment'];

$stmt = $conn->prepare("INSERT INTO reviews (product_id, user_name, rating, comment) VALUES (?, ?, ?, ?)");
$stmt->bind_param("isis", $product_id, $user_name, $rating, $comment);

if ($stmt->execute()) {
    echo "Отзыв успешно добавлен!";
} else {
    echo "Ошибка: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
