let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  let movs = data.results;
  for (let flm of movs) {
    $('ul#list_movies').append(`<li>${flm.title}</li>`);
  }
});
