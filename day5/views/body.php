<p>Body</p>
<? 
	foreach($par2 as $users){
		echo $users["username"];
		echo " <a href='?controller=home&action=updateForm&id=".$users["id"]."'>Update</a>";
		echo " <a href='?controller=home&action=delete&id=".$users["id"]."'>Delete</a>";
		echo " <br/>";
	} 
?>

