// Alumni25 main.js

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Show/hide password toggle for login/register forms
    document.querySelectorAll('input[type="password"]').forEach(input => {
        const toggle = document.createElement('span');
        toggle.textContent = '👁️';
        toggle.style.cursor = 'pointer';
        toggle.style.marginLeft = '8px';
        toggle.onclick = function() {
            input.type = input.type === 'password' ? 'text' : 'password';
        };
        input.parentNode.insertBefore(toggle, input.nextSibling);
    });

    // Simple form validation feedback
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            let valid = true;
            form.querySelectorAll('input[required], textarea[required]').forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = '#e74c3c';
                    valid = false;
                } else {
                    input.style.borderColor = '#f9d342';
                }
            });
            if (!valid) {
                e.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    });

    // Flash message auto-dismiss
    const flash = document.querySelector('.flash');
    if (flash) {
        setTimeout(() => {
            flash.style.transition = 'opacity 0.5s';
            flash.style.opacity = 0;
            setTimeout(() => flash.remove(), 500);
        }, 3500);
    }
}); 