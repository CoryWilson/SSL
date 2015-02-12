<p>Update Form</p>
<? 
	foreach($par2 as $users){
		?>
		<form action="?controller=home&action=update&id=<?echo $users['id']?>" method="POST">

			<input type="text" name="username" value="<?echo $users['username']?>" />
  			<input type="text" name="password" value="<?echo $users['password']?>" />
			<button type="submit">
				Update User
			</button>
		</form>
		<?
		// echo $users["username"];
		// echo " <a href='?controller=home&action=updateForm&id=".$users["id"]."'>Update</a>";
		// echo " <a href='?controller=home&action=delete&id=".$users["id"]."'>Delete</a>";
		// echo " <br/>";
	} 
?>
