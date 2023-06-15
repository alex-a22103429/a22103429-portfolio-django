const submitButton = document.getElementById('submit-caption');
const inputField = document.getElementById('caption-input');
const submitButton1 = document.getElementById('submit-caption1');
const inputField1 = document.getElementById('caption-input1');
const caption = document.getElementById('caption');
const caption1 = document.getElementById('caption1');
const caption2 = document.getElementById('caption2');
const caption3 = document.getElementById('caption3');



 function calcular11() {
    const userInput = inputField.value;
    caption.textContent = userInput;
    const expressao = document.getElementById('expressao').value;

  }


submitButton.addEventListener('click', function() {
  const userInput = inputField.value;
  caption.textContent = userInput;
});

submitButton1.addEventListener('click', function() {
  const userInput1 = inputField1.value;
  caption1.textContent = userInput1;
  caption2.textContent = userInput1;
  caption3.textContent = userInput1;
});
