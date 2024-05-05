<?php
$url = "http://express.heartrails.com/api/json?method=getStations&line=JR%E5%B1%B1%E6%89%8B%E7%B7%9A";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "$url");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$output = curl_exec($ch);
curl_close($ch);

$list = json_decode($output, true);
for($i=0;$i<count($list[response][station]);$i++){
	$pwk = $list[response][station][$i][y].",".$list[response][station][$i][x];
	$add_p .= "$pwk"."|";
}
$add_p = rtrim($add_p,"|");
$poly = "path=color:green|weight:5|fillcolor:0xFFFF0033|".$add_p."";
$st_url ="http://maps.googleapis.com/maps/api/staticmap?sensor=false&size=512x512&".$poly;
print("<img src=\"$st_url\">");
exit;
?>
