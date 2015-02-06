<?
  session_start();
  //home controller
  include 'models/view.php';

  $viewmodel = new view();

  if(empty($_GET["action"])){

    $viewmodel->getView("views/header.php");
    $viewmodel->getView("views/body.php");
    $viewmodel->getView("views/footer.php");

  } else{


    if($_GET["action"]=="home"){

    } else if($_GET["action"]=="loginForm"){

      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/form.php");
      $viewmodel->getView("views/footer.php");

    } else if($_GET["action"]=="processLogin"){

      //var_dump($_POST);
      if($_POST["username"]=="cory" && $_POST["password"]=="pass"){
        $_SESSION["username"] = $_POST["username"];
        $_SESSION["password"] = $_POST["password"];
        //$_SESSION["avatarUpload"] = $_POST["avatarUpload"];
        $_SESSION["loggedin"] = true;
      } else{
        $_SESSION["username"] = "";
        $_SESSION["username"] = false;
      }

      $data = $_POST;
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/profile.php",$data);
      $viewmodel->getView("views/footer.php");

    } else if($_GET["action"]=="checkProfile"){

      $data = $_SESSION;
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/profile.php",$data);
      $viewmodel->getView("views/footer.php");

    } else if($_GET["action"]=="logOut"){

      session_destroy();
      header('Location: index.php');
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php");
      $viewmodel->getView("views/footer.php");

    }

  }

?>
