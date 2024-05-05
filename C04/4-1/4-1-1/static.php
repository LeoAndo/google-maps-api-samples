<?php
$zoom=$_GET[zoom];
if($zoom == ""){
	$zoom=16;
}
$geo=$_GET[geo];
if($geo == ""){
	$geo = "35.774894,139.803085";
}
print("<html><head><title>zoom change</title></head><body>");
print("<form>");
print("<img src=\"http://maps.googleapis.com/maps/api/staticmap?zoom=".$zoom."&size=240x240&markers=".$geo."&sensor=false\">");
print("<br>Lv:<select name=zoom>");
for($i=0;$i<23;$i++){
	if($zoom == $i){
		print("<option value=$i selected>$i");
	}else{
		print("<option value=$i>$i");
	}
}
print("</select>");
print("<input type=text name=geo value=\"$geo\" size=9>");
print("<input type=submit value=\"Go\">");
print("<a href=\"static.php?zoom=".($zoom+1)."&geo=".$geo."\">[+]</a>");
print("<a href=\"static.php?zoom=".($zoom-1)."&geo=".$geo."\">[-]</a>");
print("</form>");
print("</body></html>");
?>
