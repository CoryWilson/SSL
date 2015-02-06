<div class="row">
  <h3>Hello, <? echo $par2["username"];?>!</h3>
</div>
<div class="row">
  <? var_dump($par2) ?>
  <h3>Your hashed password is: <h4><? echo sha1($par2["password"]);?></h4></h3>
</div>
