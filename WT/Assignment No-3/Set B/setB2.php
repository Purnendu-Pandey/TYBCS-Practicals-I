<?php
$str1 = $_GET["n1"];
$str2 = $_GET["sep"];
$ch = $_GET["op"];
echo "Entered string is : " . $str1;
echo "<br>";
echo "Entered separator is : " . $str2;
echo "<br>";
echo "selected option is : " . $ch;
echo "<br>";

switch ($ch) 
{
    case 1:
        split_str($str2, $str1);
        break;
    case 2:
        sep_replc($str2, $str1);
        break;
    case 3:
        last_occur($str1, $str2);
        break;
}
function split_str($str2, $str1) 
{
    $st = explode($str2, $str1);
    print_r($st);
}
echo "<br>";
function sep_replc($str2, $str1) 
{
    $s = str_replace($str2, "*", $str1);
    echo " New string is : " . $s;
}
echo "<br>";
function last_occur($str1, $str2) 
{
    $k = strrchr($str1, $str2);
    echo " Last word is : " . $k;
}
?>
