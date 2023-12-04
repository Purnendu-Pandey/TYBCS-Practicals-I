<?php
$op=$_POST['op'];
function is_odd($var)
{
    if ($var % 2 == 1)
        return $var;
}
$arr = array('a'=>1,'b'=>2,'c'=>3,'d'=>4,'e'=>5,'f'=>6,'g'=>7,'h'=>8);
$arr1 = array('l'=>11,'m'=>2,'n'=>33,'o'=>44,'p'=>5,'q'=>66,'r'=>77,'s'=>8);

switch($op)
{
    case 1:
          $a=array_chunk($arr,4);
          print_r($a);
          break;
    case 2:
          asort($arr);
          print_r($arr);
          break;
    case 3:
          print_r(array_filter($arr,"is_odd"));
          break;
    case 4:
          $y=array_merge($arr1,$arr2);
          echo "Merge element<br>";
          print_r($y);
          break;
    case 5:
          print_r(array_intersect($arr1,$arr2));
          break;
}
?>