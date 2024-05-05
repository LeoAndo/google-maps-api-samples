<?php
//moyorieki
$lat=35.6657;
$lon=139.8025;
$ll = $lat.",".$lon;
$url = "http://express.heartrails.com/api/json?method=getStations&x=".$lon."&y=".$lat."";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "$url");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$output = curl_exec($ch);
curl_close($ch);

$list = json_decode($output, true);
$color[]="orange";
$color[]="blue";
$color[]="green";
$ccnt=count($color);
for($i=0;$i<count($list[response][station]);$i++){
	$s = $i%$ccnt;
	$n = $i+1;
	$param .= "&markers=color:".$color[$s]."|";
	$param .= "label:".$n."|";
	$param .= $list[response][station][$i][y].",".$list[response][station][$i][x];
	$mon .= "<font color=".$color[$s].">".$n."</font> ";
	$mon .= $list[response][station][$i][name]."駅(".$list[response][station][$i][line].")"; 
	$mon .= $list[response][station][$i][distance]."<br>"; 
}
$mine="&markers=color:red|$lat,$lon";
$param.=$mine;
?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<?php
print("<img src=\"http://maps.googleapis.com/maps/api/staticmap?center=".$ll.$param."&sensor=false&zoom=14&size=512x512\">");
print("<br>");
print $mon;
exit;

/*
name	最寄駅名
x	最寄駅の経度 （世界測地系）
y	最寄駅の緯度 （世界測地系）
distance	指定の場所から最寄駅までの距離 （精度は 10 ｍ）
line	最寄駅の存在する路線名
*/
?>
