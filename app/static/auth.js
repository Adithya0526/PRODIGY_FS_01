document.getElementById("auth-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // Password Validation
    const passwordRegex = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{8,}$/;
    if (!passwordRegex.test(password)) {
        document.getElementById("auth-message").textContent = "Password does not meet the criteria!";
        return;
    }

    try {
        // Try to sign in or create account
        let userCredential;
        try {
            userCredential = await signInWithEmailAndPassword(auth, email, password);
            document.getElementById("auth-message").textContent = "Login successful!";
        } catch {
            userCredential = await createUserWithEmailAndPassword(auth, email, password);
            document.getElementById("auth-message").textContent = "Signup successful!";
        }

        console.log("User Info:", userCredential.user);

        // Redirect to Welcome Page
        window.location.href = "/auth/welcome";
    } catch (error) {
        document.getElementById("auth-message").textContent = `Error: ${error.message}`;
    }
});
