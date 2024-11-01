const productData = {
    "name": "Crude Oil",
    "category": "Energy",
    "quantity": 5000000,
    "unit": "barrels",
    "country_of_origin": "Saudi Arabia",
    "exported_to": ["United States", "China", "India"],
    "unit_price": 75.50,
    "total_value": 377500000,
    "description": "Unrefined petroleum oil used for fuel and energy production."
  };
  
  function populateProductCard(data) {
    document.getElementById("productName").textContent = data.name;
    document.getElementById("productCategory").textContent = "Category: " + data.category;
    document.getElementById("productCountry").textContent = "Country of Origin: " + data.country_of_origin;
    document.getElementById("productQuantity").textContent = "Available Stock: " + data.quantity + " " + data.unit;
    document.getElementById("productPrice").textContent = "Price: $" + data.unit_price.toFixed(2) + " per " + data.unit;
    document.getElementById("productTotalValue").textContent = "Total Value: $" + data.total_value.toFixed(2);
    document.getElementById("productDescription").textContent = data.description;
  
    // Populate exported countries
    document.getElementById("productExportedTo").textContent = "Exported To: " + data.exported_to.join(", ");
  }
  
  // Populate the product card on page load
  window.onload = function() {
    populateProductCard(productData);
  };
  