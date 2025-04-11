// This file contains JavaScript code for interactivity on the website. It may include functions for form validation, smooth scrolling, and other dynamic features.

document.addEventListener("DOMContentLoaded", function() {
    // Smooth Scrolling Navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Back-to-Top Button
    const backToTopButton = document.getElementById("back-to-top");
    if (backToTopButton) {
        backToTopButton.addEventListener("click", function() {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });

        window.addEventListener("scroll", function() {
            if (window.scrollY > 300) {
                backToTopButton.style.display = "block";
            } else {
                backToTopButton.style.display = "none";
            }
        });
    }

    // Form validation for the contact form
    const contactForm = document.getElementById("contact-form");
    if (contactForm) {
        contactForm.addEventListener("submit", function(e) {
            e.preventDefault();
            const name = document.getElementById("name").value;
            const email = document.getElementById("email").value;
            const message = document.getElementById("message").value;

            if (name === "" || email === "" || message === "") {
                alert("Please fill in all fields.");
            } else {
                alert("Thank you for your message!");
                contactForm.reset();
            }
        });
    }
});