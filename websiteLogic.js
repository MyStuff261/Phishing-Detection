function fetchAPI (text) {
  console.log(text);
  fetch('http://localhost:8000/classify', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text: text })
  })
  .then(response => response.json())
  .then(data => {
    document.querySelector('.js-text').innerHTML = `<p>${text}</p><p>${data.message}</p>`;
    document.querySelector('.js-text-input').value = '';
  });
}
