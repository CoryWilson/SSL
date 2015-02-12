<?
  session_start();
  //home controller
  include 'models/view.php';
  include 'models/file.php';
  include 'models/login.php';
  include 'models/users.php';

  $viewmodel = new view();
  $filemodel = new file();
  $loginmodel = new login();
  $usersmodel = new users();

  if(empty($_GET["action"])){

    $viewmodel->getView("views/header.php");
    $viewmodel->getView("views/body.php");
    $viewmodel->getView("views/footer.php");

  } else{


    if($_GET["action"]=="home"){

      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="loginForm"){

      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/form.php");
      $viewmodel->getView("views/footer.php");

    } else if($_GET["action"]=="processLogin"){

      $returnedLogin = $loginmodel->checkuser($_POST);

      if($returnedLogin){
        $_SESSION["username"] = $returnedLogin["username"];
        $_SESSION["loggedin"] = true;
      } else{
        $_SESSION["username"] = "";
        $_SESSION["username"] = false;
      }

      $data = $returnedLogin;
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/results.php", $data);
      $viewmodel->getView("views/footer.php");

    } else if($_GET["action"]=="checkSession"){

      $data = $_SESSION;
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/results.php", $data);
      $viewmodel->getView("views/footer.php");

    } else if($_GET["action"]=="outXML"){

      $data = $usersmodel->getUsers();
      header("Content-Type: text/xml");
      ?>
        <employees>
          <? foreach($data as $users){ ?>
          <person>
            <username><?= $users["username"]; ?></username>
            <password><?= $users["password"]; ?></password>
            <userimg><?= "uploads/image.jpg" ?></userimg>
          </person>
          <? } ?>
        </employees>
      <?
    } else if($_GET["action"]=="outJSON"){
      
      header("Content-Type: application/json");
      $data = $usersmodel->getUsers();
      echo json_encode($data);

    } else if($_GET["action"]=="inJSON"){

      $data = file_get_contents("http://localhost:8888/SSL/day5/?controller=home&action=outJSON");
      $JSONarr = json_decode($data, true);
      //var_dump($JSONarr);

      foreach($JSONarr as $users){
        echo "username: ".$users["username"];
        echo "<br />";
        echo "password: ".$users["password"];
        echo "<br />";
      }

    } else if($_GET["action"]=="delete"){
      $usersmodel->deleteUser($_GET["id"]);
      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="updateForm"){

      $data = $usersmodel->getUser($_GET["id"]);
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/updateForm.php", $data);

      // $data = $usersmodel->getUsers();
      // $viewmodel->getView("views/header.php");
      // $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="update"){
      $data = $usersmodel->updateUser($_POST["username"],$_POST["password"],$_GET["id"]);
      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="uploadForm"){

      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/uploadForm.php");

    } else if($_GET["action"]=="add"){
      $data = $usersmodel->addUser($_POST["username"],$_POST["password"]);
      $data = $usersmodel->getUsers();
      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/body.php", $data);

    } else if($_GET["action"]=="addForm"){

      $viewmodel->getView("views/header.php");
      $viewmodel->getView("views/addForm.php");

    } else if($_GET["action"]=="uploadAction"){

      // echo '$_POST';
      // var_dump($_POST);
      // echo '$_GET';
      // var_dump($_GET);
      // echo '$_FILES';
      // var_dump($_FILES);
      $viewmodel->getView("views/header.php");
      $filemodel->upload($_FILES);

    }

  }

?>
