document.addEventListener("DOMContentLoaded", function() {
    // Form validation for the contact section
    const contactForm = document.getElementById("contact-form");
    contactForm.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;
        
        if (name === "" || email === "" || message === "") {
            alert("Please fill in all fields.");
            return;
        }
        
        // Here you can add code to send the form data to a server or an email service
        alert("Thank you for your message, " + name + "!");
        contactForm.reset();
    });

    // Dynamic behavior for project cards
    const projectCards = document.querySelectorAll(".project-card");
    projectCards.forEach(card => {
        card.addEventListener("click", function() {
            const projectDetails = this.querySelector(".project-details");
            projectDetails.classList.toggle("visible");
        });
    });
});