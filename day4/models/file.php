<?

  class file{

    public function upload($up){

      //include $up;
    	$uploaddir = './uploads/';
    	$uploadfile = $uploaddir . basename($up['myfile']['name']);

    	if(move_uploaded_file($up['myfile']['tmp_name'], $uploadfile)){
    		echo "File is valid, and was successfully uploaded. \n";
    		?>
    		<img src="uploads/<?=$up['myfile']['name']?>"/>
    		<?

    	}
    		
    }

  }

?>
