$(document).ready(function() {
	$("input:radio[name=type]").change(function() {
		if (this.value == "business") {
			$("#tip").text("Business is selected");
		}
		if (this.value == "building") {
			$("#tip").text("Building is selected");
		}
		if (this.value == "employer") {
			$("#tip").text("Employer is selected");
		}
		if (this.value == "employee") {
			$("#tip").text("Employee is selected");
		}
	});
});