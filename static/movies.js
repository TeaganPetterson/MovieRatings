document.querySelector('#score_form').addEventListener('submit', (evt) => {
    evt.preventDefault();
  
    const formInputs = {
      movie_id: document.querySelector('#movie_id').value,
      score: document.querySelector('#score').value,
    };
  
    fetch('/ratings', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        console.log(responseJson['score']['score'])
		document.querySelector("#rating").innerText = `You rated this movie ${responseJson['score']['score']} out of 5 stars`}
      );
  });