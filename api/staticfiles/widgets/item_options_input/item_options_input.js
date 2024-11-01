const FORM_BTN = "options-add";
const FORM = "options";
const DEL_BTN = "option-remove";

document.addEventListener("DOMContentLoaded", function () {
  var addFormButton = document.getElementById(FORM_BTN);
  var formContainer = document.getElementById(FORM);
  var totalFormsInput = document.getElementById("id_form-TOTAL_FORMS");

  // Function to add a new form
  const firstFormRow = formContainer.querySelector(".form-row");

  addFormButton.addEventListener("click", function () {
    var totalForms = parseInt(totalFormsInput.value);
    // Clone the first form row

    var newFormRow = firstFormRow.cloneNode(true);
    // Clear the input values in the cloned form
    var inputs = newFormRow.querySelectorAll("input");

    inputs.forEach(function (input) {
      input.value = "";
    });

    // Update the name attributes for the new form
    inputs.forEach(function (input) {
      var name = input.name.replace(/-\d+/, "-" + totalForms);
      input.name = name;
    });

    // Append the new form row to the container
    formContainer.appendChild(newFormRow);

    // Update the total forms count
    totalFormsInput.value = totalForms + 1;
  });

  // Function to remove a form
  formContainer.addEventListener("click", function (event) {
    if (event.target.classList.contains(DEL_BTN)) {
      var formRow = event.target.closest(".form-row");
      formRow.remove();

      // Update the total forms count
      var totalForms = parseInt(totalFormsInput.value);
      totalFormsInput.value = totalForms - 1;
    }
  });
});
