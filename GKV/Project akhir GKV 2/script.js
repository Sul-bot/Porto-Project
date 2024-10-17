(function () {
	var data = [
	    { provinsi: 'Aceh', tumbuhanKopi: 71.1 },
	    { provinsi: 'Sumatera Utara', tumbuhanKopi: 87.9 },
	    { provinsi: 'Sumatera Barat', tumbuhanKopi: 23 },
	    { provinsi: 'Riau', tumbuhanKopi: 1.8 },
	    { provinsi: 'Jambi', tumbuhanKopi: 19.9 },
	    { provinsi: 'Sumatera Selatan', tumbuhanKopi: 198 },
	    { provinsi: 'Bengkulu', tumbuhanKopi: 55 },
	    { provinsi: 'Lampung', tumbuhanKopi: 108.1 },
	    { provinsi: 'Kep. Bangka Belitung', tumbuhanKopi: 0 },
	    { provinsi: 'Kep. Riau', tumbuhanKopi: 0 },
	    { provinsi: 'DKI Jakarta', tumbuhanKopi: 0 },
	    { provinsi: 'Jawa Barat', tumbuhanKopi: 22.6 },
	    { provinsi: 'Jawa Tengah', tumbuhanKopi: 26 },
	    { provinsi: 'DI Yogyakarta', tumbuhanKopi: 0.5 },
	    { provinsi: 'Jawa Timur', tumbuhanKopi: 48.1 },
	    { provinsi: 'Banten', tumbuhanKopi: 2 },
	    { provinsi: 'Bali', tumbuhanKopi: 14.5 },
	    { provinsi: 'Nusa Tenggara Barat', tumbuhanKopi: 6.5 },
	    { provinsi: 'Nusa Tenggara Timur', tumbuhanKopi: 25.1 },
	    { provinsi: 'Kalimantan Barat', tumbuhanKopi: 3.1 },
	    { provinsi: 'Kalimantan Tengah', tumbuhanKopi: 0.2 },
	    { provinsi: 'Kalimantan Selatan', tumbuhanKopi: 0.7 },
	    { provinsi: 'Kalimantan Timur', tumbuhanKopi: 0.2 },
	    { provinsi: 'Kalimantan Utara', tumbuhanKopi: 0.2 },
	    { provinsi: 'Sulawesi Utara', tumbuhanKopi: 3.6 },
	    { provinsi: 'Sulawesi Tengah', tumbuhanKopi: 3.1 },
	    { provinsi: 'Sulawesi Selatan', tumbuhanKopi: 27.5 },
	    { provinsi: 'Sulawesi Tenggara', tumbuhanKopi: 2.8 },
	    { provinsi: 'Gorontalo', tumbuhanKopi: 0.1 },
	    { provinsi: 'Sulawesi Barat', tumbuhanKopi: 4.8 },
	    { provinsi: 'Maluku', tumbuhanKopi: 0.4 },
	    { provinsi: 'Maluku Utara', tumbuhanKopi: 0 },
	    { provinsi: 'Papua Barat', tumbuhanKopi: 0 },
	    { provinsi: 'Papua Barat Daya', tumbuhanKopi: 0 },
	    { provinsi: 'Papua', tumbuhanKopi: 3.2 },
	    { provinsi: 'Papua Selatan', tumbuhanKopi: 0 },
	    { provinsi: 'Papua Tengah', tumbuhanKopi: 0 },
	    { provinsi: 'Papua Pegunungan', tumbuhanKopi: 0 },
	];
                                                  
	function drawChart(labels, dataValues) {
	    var ctx = document.getElementById('pieChart').getContext('2d');
	    new Chart(ctx, {
	        type: 'pie',
	        data: {
	            labels: labels,
	            datasets: [{
	                label: 'Tumbuhan Kopi',
	                data: dataValues,
	                backgroundColor: [
	                    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40', 
	                    '#E7E9ED', '#FF6347', '#ADFF2F', '#40E0D0', '#EE82EE', '#F5DEB3', 
	                    '#9ACD32', '#FFD700', '#FA8072', '#20B2AA', '#87CEEB', '#778899', 
	                    '#7FFF00', '#D2691E', '#8A2BE2', '#5F9EA0', '#6495ED', '#DC143C', 
	                    '#FF4500', '#2E8B57', '#48D1CC', '#00CED1', '#9400D3', '#FF1493', 
	                    '#7B68EE', '#00FF7F', '#FF5733', '#C70039', '#900C3F', '#581845',
	                    '#1F618D', '#148F77', '#117A65', '#D4AC0D'
	                ],
	            }]
	        },
	        options: {
	            responsive: true,
	            plugins: {
	                legend: {
	                    position: 'top',
	                },
	                tooltip: {
	                    callbacks: {
	                        label: function (context) {
	                            return `${context.label}: ${context.raw} ribu ton`;
	                        }
	                    }
	                }
	            }
	        }
	    });
	}
                                                  
	var labels = data.map(item => item.provinsi);
	var dataValues = data.map(item => item.tumbuhanKopi);
                                                  
	drawChart(labels, dataValues);
                                                  })();
                                                  