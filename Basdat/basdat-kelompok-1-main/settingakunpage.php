<?php
		$query = pg_query("SELECT * FROM user");
		// $query = mysqli_query($db, $sql);


		while($user = pg_fetch_array($query)){
			echo "<tr>";

			echo "<td>".$user['nama_lengkap']."</td>";
			echo "<td>".$user['username']."</td>";
			echo "<td>".$user['kata_sandi']."</td>";
			
            if (!isset($_GET['id_admin'])) {
                header('Location: settingakunpage.php');
            }
            
            $id = $_GET['id_admin'];
            
            $query = "SELECT * FROM user WHERE id_admin=$id";
            $result = pg_query($db, $query); 
            
            if (!$result) {
                die("Query failed: " . pg_last_error());
            }
            
            $siswa = pg_fetch_assoc($result);
            
            if (pg_num_rows($result) < 1) {
                die("Data tidak ditemukan...");
            }
        }
            


		?>

	</tbody>
	</table>

	<p>Total: <?php echo pg_num_rows($query) ?></p>

	</body>
</html>