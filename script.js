document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predictionForm');
    const resultContainer = document.getElementById('resultContainer');
    const predictBtn = document.getElementById('predictBtn');
    const loader = document.getElementById('loader');
    const btnText = document.querySelector('.btn-text');
    const resetBtn = document.getElementById('resetBtn');
    const scoreValue = document.getElementById('scoreValue');
    const progressCircle = document.getElementById('progressCircle');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // UI Loading State
        btnText.style.display = 'none';
        loader.style.display = 'block';
        predictBtn.disabled = true;

        // Gather Data
        const formData = {
            studentName: document.getElementById('studentName').value,
            rollNumber: document.getElementById('rollNumber').value,
            parentalEducation: document.getElementById('parentalEducation').value,
            internetAccess: document.getElementById('internetAccess').value,
            attendancePercentage: document.getElementById('attendancePercentage').value,
            previousYearPercentage: document.getElementById('previousYearPercentage').value,
            studyHours: document.getElementById('studyHours').value
        };

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (result.success) {
                showResult(result.presentPercentage);
            } else {
                alert('Error: ' + result.error);
                resetFormState();
            }

        } catch (error) {
            console.error('Error:', error);
            alert('Failed to connect to the server.');
            resetFormState();
        }
    });

    resetBtn.addEventListener('click', () => {
        resultContainer.classList.add('hidden');
        form.classList.remove('hidden');
        resetFormState();
        form.reset();
    });

    function showResult(percentage) {
        form.classList.add('hidden');
        resultContainer.classList.remove('hidden');

        // Animate Circle
        // Circumference = 2 * pi * r = 2 * 3.14 * 70  approx 440
        const circumference = 440;
        const offset = circumference - (percentage / 100) * circumference;

        // Count up animation
        let count = 0;
        const interval = setInterval(() => {
            if (count >= percentage) {
                clearInterval(interval);
                scoreValue.innerText = percentage;
            } else {
                count++;
                scoreValue.innerText = count;
            }
        }, 15);

        // SVG Animation
        setTimeout(() => {
            progressCircle.style.strokeDashoffset = offset;
        }, 100);

        // Color based on score
        if (percentage < 60) {
            progressCircle.style.stroke = '#ff4b4b'; // Red
        } else if (percentage < 80) {
            progressCircle.style.stroke = '#ffa500'; // Orange
        } else {
            progressCircle.style.stroke = '#00ff88'; // Green
        }
    }

    function resetFormState() {
        btnText.style.display = 'block';
        loader.style.display = 'none';
        predictBtn.disabled = false;
        progressCircle.style.strokeDashoffset = 440; // Reset circle
    }
});
