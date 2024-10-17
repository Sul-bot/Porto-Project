document.getElementById('calculate').addEventListener('click', function() {
    const vehicleType = document.getElementById('vehicle-type').value;
    const distance = parseFloat(document.getElementById('distance').value);
    let carbonFootprint = 0;
  
    if (vehicleType === 'motorcycle') {
      carbonFootprint = distance * 103;
    } else if (vehicleType === 'electric-car') {
      carbonFootprint = distance * 53;
    } else if (vehicleType === 'car') {
      carbonFootprint = distance * 192;
    } else if (vehicleType === 'bus') {
      carbonFootprint = distance * 105;
    }
  
    document.getElementById('carbon-footprint').textContent = carbonFootprint.toFixed(2)+ " gram";
  });
  
  document.getElementById('vehicle-type').addEventListener('change', function() {
    var select = this;
    var selectedIndex = select.selectedIndex;
    var selectedOption = select[selectedIndex];
    selectedOption.style.color = '#4caf50';
  });
  