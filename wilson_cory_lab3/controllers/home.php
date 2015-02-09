<?
  session_start();
  include 'models/view.php';
  include 'models/file.php';
  include 'models/login.php';

  $viewmodel = new view();
  $filemodel = new file();
  $loginmodel = new login();

  if(empty($_GET["action"])){

    $viewmodel->getView("views/header.php");
    $viewmodel->getView("views/body.php");

  } else{


    if($_GET["action"]=="home"){

    } else if($_GET["action"]=="loginForm"){

      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/form.php");

    } else if($_GET["action"]=="processLogin"){

      $returnedLogin = $loginmodel->checkuser($_POST);  

      if($returnedLogin){
        $_SESSION["username"] = $_POST["username"];
        $_SESSION["loggedin"] = true;
      } else{
        $_SESSION["username"] = "";
        $_SESSION["loggedin"] = false;
      }

      $data = $returnedLogin;
      $viewmodel->getView("views/loginCheck.php",$data);
      $viewmodel->getView("views/header.php");
      $data = $_SESSION;
      $viewmodel->getView("views/profile.php",$data);


    } else if($_GET["action"]=="checkProfile"){

      $data = $_SESSION;
      $viewmodel->getView("views/loginCheck.php",$data);
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/profile.php",$data);

    } else if($_GET["action"]=="logOut"){

      session_destroy();
      header('Location: index.php?controller=home');
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php");

    }

  }

?>
