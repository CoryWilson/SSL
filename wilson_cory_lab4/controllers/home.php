<?
  session_start();
  include 'models/view.php';
  include 'models/users.php';

  $viewmodel = new view();
  $usersmodel = new users();

  if(empty($_GET["action"])){

    $data = $usersmodel->getUsers();
    $viewmodel->getView("views/header.php");
    $viewmodel->getView("views/body.php", $data);
    
  } else{


    if($_GET["action"]=="home"){

      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);
      
    } else if($_GET["action"]=="delete"){
      $usersmodel->deleteUser($_GET["id"]);
      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="updateForm"){

      $data = $usersmodel->getUser($_GET["id"]);
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/updateForm.php", $data);

    } else if($_GET["action"]=="update"){
      $data = $usersmodel->updateUser($_POST["username"],$_POST["password"],$_GET["id"]);
      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="add"){
      $data = $usersmodel->addUser($_POST["username"],$_POST["password"]);
      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="addForm"){

      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/addForm.php");

    }

  }

?>
