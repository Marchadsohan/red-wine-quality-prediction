document.getElementById('wineForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const features = document.getElementById('features').value.split(',').map(Number);

    if (features.some(isNaN)) {
        document.getElementById('result').textContent = 'Please enter valid numeric features.';
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features }),
        });

        const data = await response.json();
        document.getElementById('result').textContent = `Predicted Quality: ${data.quality}`;
    } catch (error) {
        document.getElementById('result').textContent = 'Error fetching prediction. Please try again.';
        console.error(error);
    }
});
