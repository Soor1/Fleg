let searchButton = document.getElementById('search-button');
let filterButton = document.getElementById('filter-button');
let searchBar = document.getElementById('search-bar');

searchButton.addEventListener('click', () => {
    let nameSearch = searchBar.value;
    console.log(nameSearch)
});

filterButton.addEventListener('click', () => {
    console.log("filter clicked");
});