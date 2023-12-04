<?php
$str = $_GET["n1"];
$ch = $_GET["op"];
echo "Entered string is : " . $str;
echo "<br>";
echo "selected option is : " . $ch;
echo "<br>";

switch ($ch)
{
    case 1:
        length($str);
        break;
    case 2:
        count_vowels($str);
        break;
    case 3:
        lowr_case($str);
        break;
    case 4:
        pad($str);
        break;
    case 5:
        rem_whit_space($str);
        break;
    case 6:
        rev($str);
        break;
}
function length($str)
{
    $len = strlen($str);
    $cnt = 0;
    for ($i = 0; $i < $len; $i++)
        $cnt++;
    echo "length of string is : " . $cnt;
}
echo "<br>";
function count_vowels($str) 
{
    $cn = 0;
    $len = strlen($str);
    for ($i = 0; $i < $len; $i++)
        if ($str[$i] == "a" || $str[$i] == "e" || $str[$i] == "i" || $str[$i] == "o" || $str[$i] == "u")
            $cn++;
    echo "vowel count is : " . $cn;
}
echo "<br>";
function lowr_case($str) 
{
    $st = strtolower($str);
    echo " string in lowercase is :" . $st;
    echo "<br>";
    $s = ucwords($str);
    echo " Titlecase string is " . $s;
}
function rev($str) 
{
    $str = strrev($str);
    echo " Reverse string is : " . $str;
}
function pad($str) 
{
    $p = str_pad($str, 20, "*", STR_PAD_BOTH);
    echo " Paded string with * is : " . $p;
}
function rem_whit_space($str) 
{
    $k = str_replace(" ", "", $str);
    echo "String without whit space removing from start is : " . $str;
    echo "<br>";
    echo "String after removing white space from start is : " . $k;
}
?>
