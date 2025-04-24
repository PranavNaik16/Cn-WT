<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = htmlspecialchars($_POST['name']);
  $email = htmlspecialchars($_POST['email']);
  $message = htmlspecialchars($_POST['message']);

  $to = "your_email@example.com";  // Replace with your email
  $subject = "New Contact Form Submission";
  $body = "Name: $name\nEmail: $email\nMessage:\n$message";
  $headers = "From: $email";

  if (mail($to, $subject, $body, $headers)) {
    echo "<p style='color: green; text-align: center;'>Message sent successfully!</p>";
  } else {
    echo "<p style='color: red; text-align: center;'>Failed to send message.</p>";
  }
}
?>