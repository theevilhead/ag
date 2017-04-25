<?PHP 

$d["sensor_1"] = $_GET["h"];
$d["sensor_2"] = $_GET["m"];
$d["sensor_3"] = $_GET["t"];
$con = new mysqli("localhost","root","akshay","sensor_data");

$d = json_encode($d);

$qry  = sprintf('INSERT INTO sensor_data (uid,auth_id,sdata,sdate,stime) VALUES(56789,"znjMki9sdjer44',CURRENT_DATE,CURRENT_TIME));
$res = $con->query($qry);



?>
