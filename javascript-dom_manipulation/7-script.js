const movieList = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const item = document.createElement('li');
      item.textContent = movie.title;
      movieList.appendChild(item);
    });
  });
