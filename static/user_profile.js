/**
 * User Profile JavaScript functionality
 * Handles user profile data and interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the user profile page
    if (window.location.href.includes('user_profile')) {
        initUserProfile();
    }
});

function initUserProfile() {
    console.log('Initializing User Profile page');
    
    // Load user data
    loadUserData();
    
    // Initialize profile image upload
    initProfileImageUpload();
    
    // Initialize form validation
    initFormValidation();
}

function loadUserData() {
    // This would typically be an AJAX call to fetch user data
    console.log('Loading user data...');
    
    // Simulate loading data
    setTimeout(() => {
        console.log('User data loaded');
        // Update UI with the loaded data
    }, 1000);
}

function initProfileImageUpload() {
    const uploadBtn = document.querySelector('.btn-block');
    
    if (uploadBtn) {
        uploadBtn.addEventListener('click', function() {
            // Create a file input element
            const fileInput = document.createElement('input');
            fileInput.type = 'file';
            fileInput.accept = 'image/*';
            
            // Trigger click on the file input
            fileInput.click();
            
            // Handle file selection
            fileInput.addEventListener('change', function() {
                if (this.files && this.files[0]) {
                    const file = this.files[0];
                    
                    // Preview the image
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        const profilePic = document.querySelector('.profile-picture');
                        if (profilePic) {
                            profilePic.src = e.target.result;
                        }
                    };
                    reader.readAsDataURL(file);
                    
                    // Upload the image (this would be an AJAX call in a real implementation)
                    console.log('Uploading profile image:', file.name);
                }
            });
        });
    }
}

function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Basic validation example
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    // Add error styling
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                console.log('Form validation failed');
            } else {
                console.log('Form validation passed');
            }
        });
    });
}