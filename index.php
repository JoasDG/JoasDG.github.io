<!DOCTYPE html>
<html lang="en">

<?php

     $website='

  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SCRUM</title>
    <link rel="icon" href="../images/S.png" type="image/x-icon">
    <link rel="stylesheet" href="style.css">
  </head>

  <body>

    <div class="header">
      <h1>SCRUM</h1>
    </div>

    <div class="row">
      <div class="leftcolumn">
        <div class="clickable-card">
          <h2>Vacation Generator</h2>
          <p>This generator will generate the best vacation location based on your input! Just say where you want to go
            and the
            generator will do the rest.</p>
          <img src="https://picsum.photos/530/345?grayscale" alt="VacationImage" position="top">
        </div>
        <div class="card">
          <h2>Contact Us</h2>
          <p>Have any questions? Feel free to contact us!</p>
          <form action="../index.php" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
            <br />
            <br />
            <label for="email">Email:</label>
            <input type="email" id="email" name="email">
            <br />
            <br />
            <label for="message">Message:</label>
            <textarea id="message" name="textarea"></textarea>
            <br />
            <br />
            <input type="submit" value="Send" onclick="myFunction()" value="Show alert box">
          </form>
        </div>
      </div>
      <div class="row">
        <div class="rightcolumn">
          <div class="card">
            <h2>About Us</h2>
            <p>We are a group of students from the Computer Science class at CCollege. We are trying to create a website
              for
              a
              vacation generator.</p>
          </div>
          <div class="card">
            <h2>Follow Us</h2>
            <p><i>Invalid input</i></p>
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <h2>&#169; 2024 The SCRUM Group</h2>
    </div>

  </body>
  ';
  
 if ($_SERVER["REQUEST_METHOD"] != "POST") {

 echo $website;
 }
 else {
   $name = $_POST['name'];
   $email = $_POST['email'];
   $message = $_POST['textarea'];

   echo "<div id='ga-weg' style='background-color:#FAFAFA; position:absolute; top:50px; left:50px;  border-radius:10px; border-color:black; border-style:ridge; padding:5px; opacity:1; transition: opacity 2s ease-in-out;'>Thank you for your message, $name!<br><br>Message: <i>\"$message\"</i></div>";

   $open = fopen("nr.txt", "a");
   fwrite($open, "$name ($email) has messaged: \"$message\"\n");
   fclose($open);

   echo $website;

   echo '<script>
       setTimeout(function() {
           var element = document.getElementById("ga-weg");
           element.style.opacity = "0";
           setTimeout(function() {
               element.style.display = "none";
           }, 2000);
       }, 5000);
   </script>'; }
?>
</html>