<?php
$eventTitle=$_GET['e1'];
$con = pg_connect("host=192.168.1.254 dbname=ty32 user=ty32 password=123456");
if ($con)
{
    echo "Able to open database\n"; 
}
else
{
    echo "Unable to open database \n";
}

$sql = <<<EOF
	select *from event;
	select *from committee;
EOF;
$ret = pg_query($con, $sql);
if (!$ret)
{
    echo pg_last_error($con);
}
else
{
    echo "<br>Record Created Successfully !!";
}
//$updateSql = "UPDATE COMMITTEE SET STATUS='Working';";
$updateSql = "UPDATE COMMITTEE SET STATUS='Working' WHERE CNO IN (SELECT CNO FROM EC WHERE ENO IN (SELECT ENO FROM EVENT WHERE TITLE = '$eventTitle'));";

$ret = pg_query($con, $updateSql);
if (!$ret)
{
    echo pg_last_error($con);
    exit;
}
else
{
    echo "Status updated successfully \n";
}
pg_close($con);
?>
