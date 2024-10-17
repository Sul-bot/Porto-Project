<?php
include("config.php");


if(isset($_POST['submit'])&&!empty($_POST['submit'])){
    
    $Username = md5($_POST['Username']);
    $query = pg_query("SELECT FROM User where Email = '".pg_escape_string($_POST['Email'])."' and password ='".$Password."'");
    $data = pg_query($db,$query); 
    $login_check = pg_num_rows($data);
    if($login_check > 0){ 
        
        echo "<meta http-equiv='refresh' content='0; http://localhost/Dashboard.php>";    
    }else{
        
        echo "Invalid Details";
    }
}
?>