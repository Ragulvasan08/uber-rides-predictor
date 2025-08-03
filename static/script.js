// Form submission with loading state
document.getElementById('predictionForm').addEventListener('submit', function(e) {
    const submitBtn = document.getElementById('submitBtn');
    const buttonText = submitBtn.querySelector('.button-text');
    const loadingSpinner = submitBtn.querySelector('.loading-spinner');
    
    // Show loading state
    buttonText.style.display = 'none';
    loadingSpinner.style.display = 'inline-block';
    submitBtn.disabled = true;
    
    // Re-enable after a timeout (in case of errors)
    setTimeout(function() {
        buttonText.style.display = 'inline-block';
        loadingSpinner.style.display = 'none';
        submitBtn.disabled = false;
    }, 10000);
});

// Input validation feedback
const inputs = document.querySelectorAll('.form-input');
inputs.forEach(function(input) {
    input.addEventListener('input', function() {
        if (this.checkValidity()) {
            this.classList.remove('invalid');
            this.classList.add('valid');
        } else {
            this.classList.remove('valid');
            this.classList.add('invalid');
        }
    });
});

// Modal functions
function closeModal() {
    const modal = document.getElementById('predictionModal');
    if (modal) {
        modal.classList.add('modal-closing');
        setTimeout(function() {
            modal.style.display = 'none';
            modal.classList.remove('modal-closing');
        }, 300);
    }
}

function newPrediction() {
    // Clear form and close modal
    document.getElementById('predictionForm').reset();
    inputs.forEach(function(input) {
        input.classList.remove('valid', 'invalid');
    });
    closeModal();
}

// Auto-show modal if prediction exists
function showPredictionModal() {
    const modal = document.getElementById('predictionModal');
    if (modal) {
        setTimeout(function() {
            modal.style.display = 'flex';
            modal.classList.add('modal-showing');
        }, 500);
    }
}

// Close modal on overlay click
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('modal-overlay')) {
        closeModal();
    }
});

// Close modal on Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Initialize modal if it exists
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('predictionModal');
    if (modal) {
        showPredictionModal();
    }
}); 