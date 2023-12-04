<?php
$str1 = $_GET['n1'];
$str2 = $_GET['n2'];
$str3 = $_GET['n3'];

function accept($str1, $str2, $str3)
{
    $p = func_get_args();
    if ($p[0] == NULL || $p[1] == NULL || $p[2] == NULL)
    {
        echo "One parameter is Missing...<br><br>";
    } 
    else 
    {
        echo $str3 . $str1;
    }
}
accept($str1, $str2, $str3);
?>
