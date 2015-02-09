<?

  class file{

    public function upload($up){

        $uploaddir = './uploads/';
        $uploadfile = $uploaddir . basename($up['myfile']['name']);

        if(move_uploaded_file($up['myfile']['tmp_name'], $uploadfile)){
            ?>
            <img src="uploads/<?=$up['myfile']['name']?>"/>
            <?
        }
            
    }

  }

?>
