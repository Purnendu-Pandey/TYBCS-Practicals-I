<?php
$a  = $_GET["n1"];
$b  = $_GET["n2"];
$ch = $_GET["op"];
echo "num_1 : " . $a;
echo "<br>";
echo "num_2 : " . $b;
echo "<br>";
echo "selected option is : " . $ch;
echo "<br>";

switch ($ch)
{
    
    case 1:
        mod($a, $b);
        break;
    case 2:
        sum($a);
        break;
    case 3:
        factorial($b);
        break;
    case 4:
        power($a, $b);
        break;
        
        
}

function mod($a, $b)
  {
    $md = $a % $b;
    echo "mod is : " . $md;
    
  }

echo "<br>";
function sum($a)
{
    $sm = 0;
    for ($i = 0; $i <= $a; $i++)
        $sm += $i;
    echo "sum is : " . $sm;
}

echo "<br>";
function factorial($b)
{
    $fact = 1;
    for ($i = 1; $i <= $b; $i++)
        $fact *= $i;
    echo "factorial of $b is : " . $fact;
}

function power($a, $b)
{
    $f = 1;
    $n = $b;
    for ($i = 1; $i <= $n; $i++)
        $f *= $a;
    echo "power of $a raised to $b is : " . $f;
}
?>
