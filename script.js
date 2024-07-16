function convertCurrency() {
  const fromCurrency = document.getElementById('from').value;
  const toCurrency = document.getElementById('to').value;
  const amount = document.getElementById('amount').value;

  // Fetch the conversion rate using an API (replace with your API call)
  fetch(`https://your-currency-api.com/convert?from=${fromCurrency}&to=${toCurrency}`)
    .then(response => response.json())
    .then(data => {
      const conversionRate = data.rate;
      const convertedAmount = amount * conversionRate;
      const resultElement = document.getElementById('result');
      resultElement.textContent = `${amount} ${fromCurrency} is equal to ${convertedAmount.toFixed(2)} ${toCurrency}`;
    })
    .catch(error => {
      console.error('Error fetching conversion rate:', error);
      const resultElement = document.getElementById('result');
      resultElement.textContent = 'An error occurred. Please try again later.';
    });
}
