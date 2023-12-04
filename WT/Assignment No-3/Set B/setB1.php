<?php
$str1 = $_GET["n1"];
$str2 = $_GET["n2"];
$ch = $_GET["op"];
echo "Entered string_1 is : " . $str1;
echo "<br>";
echo "Entered string_2 is : " . $str2;
echo "<br>";
echo "selected option is : " . $ch;
echo "<br>";

switch ($ch)
{
    case 1:
        sml_at_start($str1, $str2);
        break;
    case 2:
        sml_pos_in_bigstr($str1, $str2);
        break;
    case 3:
        comp_n_char($str1, $str2);
        break;
}
function sml_at_start($str1, $str2) 
{
    $pos = strpos($str1, $str2);
    if ($pos === 0) 
    {
        echo "  string $str2 is found at start and its position is : " . ($pos + 1);
    } 
    else 
    {
        echo "  string $str2 is not found at starting position ";
    }
}
echo "<br>";
function sml_pos_in_bigstr($str1, $str2) 
{
    $p = strpos($str1, $str2);
    if ($p !== false) 
    {
        echo "  string $str2 is found at position  : " . ($p + 1);
    } 
    else 
    {
        echo "  string $str2 is not found  ";
    }
}
echo "<br>";
function comp_n_char($str1, $str2) 
{
    $po = strncasecmp($str1, $str2, 10);
    if ($po == 0) 
    {
        echo " Both strings are equal  : ";
    } 
    else 
    {
        echo " Both strings are not equal  ";
    }
}
?>
