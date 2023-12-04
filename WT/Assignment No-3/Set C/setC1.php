
<html>
<body>
<table border=1 cellpadding=10 style="text-align:center;">
<?php
$a=$_GET["sr"];
$b=$_GET["sb"];
$c=$_GET["mr"];



$k=implode(",", $c);//marks array
$k1=explode("," , $k);
$m=implode(",", $b);// sub array
$m1=explode("," , $m);
$n=implode(",", $a); // sr no. array
$n1=explode("," , $n);

//print_r($n1);

$cn=count($n1);
$total=0;


echo " Student Result is ::  ";
echo"<br>";

//print_r($k1);


echo "
        <tr>
            <th> Sr No. </th>
            <th> Subj. Nm  </th>
             <th> Marks </th>
             <th> Total  </th>
              <th> Per </th>
              <th> Grd  </th>
        </tr>";
        
for($i=0;$i<$cn;$i++)
     $total+=$k1[$i];
$per=$total/$cn;
//gradr
if($per >= 70)
       $gd="A";
else if($per < 70)
         $gd="B";
else if($per <= 50)
         $gd="C";
else
    $gd="FAIL";

        
for($i=0;$i<$cn;$i++)
{
    if($i==0)
    
        echo "
     
      <tr > 
      
         <td > $n1[$i] </td>
         <td > $m1[$i] </td>
        <td> $k1[$i] </td>
        <td rowspan=10>  $total </td>
        <td rowspan=10>  $per </td>
        <td rowspan=10>  $gd </td>
        
        
     </tr>
      
    ";
    else
 {
       echo "
        
         <tr> 
            <td> $n1[$i] </td>
            <td> $m1[$i] </td>
           <td> $k1[$i] </td>
       
        </tr>
         
       ";
    
 }
}
?>
</table>
<html>
</body>
