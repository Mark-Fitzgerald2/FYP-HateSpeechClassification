<?php
if(!isset($_POST['submit']))
{
	//This page should not be accessed directly. Need to submit the form.
	echo "error; you need to submit the form!";
}
$name = testInput($_POST['name']);
$visitor_email = testInput($_POST['email']);
$UserMessage= testInput($_POST['UserMessage']);

//Validation
if(empty($name)||empty($visitor_email)||empty($UserMessage))
{
    echo "Name, email and user message are mandatory!";
    exit;
}

$email_from = "$visitor_email";//<== update the email address
$email_subject = "New Form submission from $name.";
$email_body = "You have received a new message from the user $name.\n".
    "Here is the message:\n $UserMessage\n".
    "The email address used was:\n $visitor_email \n".
    
$to = "m.fitzgerald24@nuigalway.ie";//<== update the email address
$headers = "From: $email_from \r\n";
$headers .= "Reply-To: $visitor_email \r\n";
//Send the email!
mail($to,$email_subject,$email_body,$headers);
//done. redirect to thank-you page.
echo "<script type='text/javascript'>window.location = 'index.html';</script>";


// remove injection
function testInput($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

?> 