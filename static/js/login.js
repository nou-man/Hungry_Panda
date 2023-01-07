function toggleForm() {
    var loginForm = document.getElementById("login-form");
    var signupForm = document.getElementById("signup-form");
    if (signupForm.style.display === "none") {
      loginForm.style.display = "none";
      signupForm.style.display = "block";
    }
    else {
        loginForm.style.display = "block";
      signupForm.style.display = "none";
    }

}