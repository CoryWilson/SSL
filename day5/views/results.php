<?
  var_dump($par2);
?>
<p>results</p>
<?

  //echo md5($par2["password"]);
  echo sha1($par2["password"]);

  //login->hash->check hash in database

?>
