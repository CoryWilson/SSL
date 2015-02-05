<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Cory Wilson | Lab 1</title>
	<link rel="stylesheet" href="css/foundation.min.css" type="text/css" />
	<link rel="stylesheet" href="css/main.css" type="text/css" />
	<script src="//use.typekit.net/jpd4eaw.js"></script>
	<script>try{Typekit.load();}catch(e){}</script>
</head>
<body>

<?

	function store_assoc_array(){
		$assocArray = []; // could also use $theArray = array();
		foreach($_POST as $key => $value){
			$assocArray[$key] = $value;
		}
		return $assocArray;
	}

	$array = store_assoc_array();
?>
	<div class='output small-12 small-centered medium-10 medium-centered large-8 large-centered columns'>
<?
	foreach($array as $key => $value){
?>
	<div class="row">
		<?='The Key is:'.$key.' & The Value is: '.$value.'.';?>
	</div>
<?
	}
	if($array["state"] == "FL"){
		?>
			<div class="row">Florida is the Sunshine State.</div>
		<?
	}
	if($array["state"] == "NY"){
		?>
			<div class="row">New York is the Empire State.</div>
		<?
	}
?>
	</div>


</body>
</html>
