function calculateBMI() {
    const heightInput = document.getElementById("heightInput").value;
    const weightInput = document.getElementById("weightInput").value;

    if (heightInput === "" || weightInput === "") {
        alert("Please enter both height and weight.");
        return;
    }

    const heightInCm = parseFloat(heightInput);
    const weightInKg = parseFloat(weightInput);

    const heightInMeter = heightInCm / 100;
    const bmi = (weightInKg / (heightInMeter * heightInMeter)).toFixed(1);

    let resultMessage = "";
    if (bmi < 18.5) {
        resultMessage = "underweight";
    } else if (bmi >= 18.5 && bmi < 25) {
        resultMessage = "normal (healthy) weight";
    } else if (bmi >= 25 && bmi < 30) {
        resultMessage = "overweight";
    } else {
        resultMessage = "obese";
    }

    const resultElement = document.getElementById("result");
    resultElement.textContent = `Your BMI is ${bmi}. You are ${resultMessage}.`;
}