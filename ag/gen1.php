<?PHP 

$d["sensor_1"] = $_GET["s_1"];
$d["sensor_2"] = $_GET["s_2"];
$d["sensor_3"] = $_GET["s_3"];

$auth = $_GET["auth_id"];

$con = new mysqli("localhost","root","girish","hack");

$d = [];
$d[0] = mt_rand(23,18);
$d[1] = mt_rand(31,38);
$d[2] = mt_rand(450,1100);

$dd = json_encode($d);


$qry = sprintf("INSERT INTO sensor_data (uid,auth_id,sdata,sdate,stime) VALUES(56789,'%s','%s',CURRENT_DATE,CURRENT_TIME)",$auth,$dd);

$res = $con->query($qry);


?>