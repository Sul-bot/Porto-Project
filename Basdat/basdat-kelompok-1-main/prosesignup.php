<?php
include("config.php");
// cek apakah tombol submit sudah diklik atau blum?
if(isset($_POST['submit'])){

	// ambil data dari form
	$Email = $_POST['Email'];
	$Username = $_POST['Username'];
	$Kata_Sandi = $_POST['Kata_Sandi'];
	
    // bikin query
  $query = pg_query("INSERT INTO User (Email, Username, Kata_Sandi) VALUEs ('$Email', '$Username', '$Kata_Sandi')");

	// cek query
	if( $query==TRUE ) {
		// kalau berhasil alihkan ke halaman index.php dengan status=sukses
		header('Location: index.php?status=sukses');
	} else {
		// kalau gagal alihkan ke halaman indek.ph dengan status=gagal
		header('Location: index.php?status=gagal');
	}


} else {
	die("Akses dilarang...");
}
?>