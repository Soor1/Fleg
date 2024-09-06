let searchButton = document.getElementById("search-button");
let filterDropdown = document.getElementById("filter-dropdown");
let searchBar = document.getElementById("search-bar");
let userSearch;
let filter;

searchButton.addEventListener("click", () => {
    userSearch = searchBar.value;
});

filterDropdown.addEventListener("click", () => {
    filter = filterDropdown.value;
});

function search(filter) {}
