<?php
$db=pg_connect('host=localhost dbname=User user=postgres password=apkkpa04');
if( !$db ){
    die("Gagal terhubung dengan database: " . pg_connect_error());
}
?>
