<?php
$fnm=$_GET["t1"];
echo "file name is:<br>",$fnm;
echo"<br>";
$fp=fopen($fnm,"r");
if(!$fp)
echo "file does not exist....";
else
{
	$fs=filesize($fnm);
	echo "contents of file:<br>";
	echo fread($fp,$fs);
	echo "<br><br>";
	echo "filesize is :<br>".$fs;
}
?>
