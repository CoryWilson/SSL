<?
  //application entry point
  //apache looks for index
  //windows/iis looks for default
  if(!empty($_GET["controller"])){
    if($_GET["controller"]=="home"){
      include 'controllers/home.php';
    } else{
      include 'controllers/home.php';
    }
  } else{
    include 'controllers/home.php';
  }
?>
