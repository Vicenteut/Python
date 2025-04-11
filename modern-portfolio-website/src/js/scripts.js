// This file contains JavaScript code for interactivity on the website. It may include functions for form validation, smooth scrolling, and other dynamic features.

document.addEventListener("DOMContentLoaded", function() {
    // Smooth scrolling for navigation links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            const targetId = this.getAttribute("href");
            const targetElement = document.querySelector(targetId);
            targetElement.scrollIntoView({ behavior: "smooth" });
        });
    });

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