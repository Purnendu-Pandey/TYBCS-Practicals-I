<?php
    $ch=$_POST["op"];
    $a=array("Sophia"=>31,"Jacod"=>41,"William"=>39,"Ramesh"=>40);
    print_r($a);
    switch($ch)
    {
         case 1:
         	asort($a);
         	echo "<br>Ascending Order sort by<b>value</b>:";
         	print_r($a);
         	break;
         case 2:
         	ksort($a);
         	echo "<br>Ascending Order sort by<b>key</b>:";
         	print_r($a);
         	break;
         case 3:
         	arsort($a);
         	echo "<br>Descending Order sorting by<b>value</b>:";
         	print_r($a);
         	break;
         case 4:
         	krsort($a);
         	echo "<br>Descending Orderting sort by<b>key</b>:";
         	print_r($a);
         	break;
         
     }
?> 

