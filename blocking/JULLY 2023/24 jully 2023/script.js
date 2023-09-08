function convertToFahrenheit() {
    const fahrenheitInput = document.getElementById("fahrenheitInput").value;
    if (fahrenheitInput === "") {
        alert("Please enter a temperature in Fahrenheit.");
        return;
    }

    const fahrenheit = parseFloat(fahrenheitInput);
    const celsius = ((fahrenheit - 32) * 5 / 9).toFixed(2);

    const resultElement = document.getElementById("result");
    resultElement.textContent = `${fahrenheit} degrees Fahrenheit is approximately ${celsius} degrees Celsius.`;
}