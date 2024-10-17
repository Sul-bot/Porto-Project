(function () {
    var data = [
        { provinsi: 'Aceh', tumbuhanKopi: 200 },
        { provinsi: 'Sumatera Utara', tumbuhanKopi: 300 },
        { provinsi: 'Sumatera Barat', tumbuhanKopi: 150 },
        { provinsi: 'Riau', tumbuhanKopi: 100 },
        { provinsi: 'Jambi', tumbuhanKopi: 120 },
        { provinsi: 'Sumatera Selatan', tumbuhanKopi: 180 },
        { provinsi: 'Bengkulu', tumbuhanKopi: 90 },
        { provinsi: 'Lampung', tumbuhanKopi: 160 },
        { provinsi: 'Bangka Belitung', tumbuhanKopi: 70 },
        { provinsi: 'Kepulauan Riau', tumbuhanKopi: 50 },
        { provinsi: 'DKI Jakarta', tumbuhanKopi: 30 },
        { provinsi: 'Jawa Barat', tumbuhanKopi: 210 },
        { provinsi: 'Jawa Tengah', tumbuhanKopi: 220 },
        { provinsi: 'DI Yogyakarta', tumbuhanKopi: 80 },
        { provinsi: 'Jawa Timur', tumbuhanKopi: 250 },
        { provinsi: 'Banten', tumbuhanKopi: 60 },
        { provinsi: 'Bali', tumbuhanKopi: 130 },
        { provinsi: 'Nusa Tenggara Barat', tumbuhanKopi: 110 },
        { provinsi: 'Nusa Tenggara Timur', tumbuhanKopi: 100 },
        { provinsi: 'Kalimantan Barat', tumbuhanKopi: 140 },
        { provinsi: 'Kalimantan Tengah', tumbuhanKopi: 120 },
        { provinsi: 'Kalimantan Selatan', tumbuhanKopi: 110 },
        { provinsi: 'Kalimantan Timur', tumbuhanKopi: 90 },
        { provinsi: 'Kalimantan Utara', tumbuhanKopi: 80 },
        { provinsi: 'Sulawesi Utara', tumbuhanKopi: 70 },
        { provinsi: 'Sulawesi Tengah', tumbuhanKopi: 150 },
        { provinsi: 'Sulawesi Selatan', tumbuhanKopi: 170 },
        { provinsi: 'Sulawesi Tenggara', tumbuhanKopi: 60 },
        { provinsi: 'Gorontalo', tumbuhanKopi: 50 },
        { provinsi: 'Sulawesi Barat', tumbuhanKopi: 40 },
        { provinsi: 'Maluku', tumbuhanKopi: 30 },
        { provinsi: 'Maluku Utara', tumbuhanKopi: 20 },
        { provinsi: 'Papua', tumbuhanKopi: 10 },
        { provinsi: 'Papua Barat', tumbuhanKopi: 5 }
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
                        '#7B68EE', '#00FF7F'
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
                                return `${context.label}: ${context.raw}`;
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
