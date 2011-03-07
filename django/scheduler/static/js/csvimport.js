$(document).ready(function() {
	$("input:radio[name=type]").change(function() {
		if (this.value == "business") {
			$("#tip").html("Hello world0");
		}
		if (this.value == "building") {
			$("#tip").html("Hello world1");
		}
		if (this.value == "employer") {
			$("#tip").html("Hello world2");
		}
		if (this.value == "employee") {
		alert("success");
			$("#tip").text("Hello world3");
		}
		else {
			$("#tip").html("Hello world4");
		}
	});
});