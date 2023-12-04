<?php
    $a=array(1,3,4,5,7);
    echo "<br> Original Array :";
    print_r($a);
    $b=array(11);
    array_splice($a,3,0,$b);
    echo "<br> After inserting array :";
    print_r($a);
?>
    
    
    
