<?

	function store_assoc_array(){
		$assocArray = []; // could also use $theArray = array();
		foreach($_POST as $key => $value){
			$assocArray[$key] = $value;
		}
		return $assocArray;
	}

	$array = store_assoc_array();

	foreach($array as $key => $value){
		echo "The Key is: $key & The Value is: $value<br/>";
	}
	if($array["state"] == "FL"){
		echo "Sunshine State";
	}
	if($array["state"] == "NY"){
		echo "Empire State";
	}

?>