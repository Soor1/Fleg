document.addEventListener("DOMContentLoaded", function() {
    const searchButton = document.getElementById("search-button");
    const searchInput = document.getElementById("search-input");
    let searchType = "all"; // Default search type

    document.querySelectorAll(".dropdown-content a").forEach(item => {
        item.addEventListener("click", function(event) {
            searchType = event.target.getAttribute("data-search");
            document.querySelector(".dropbtn").textContent = `Search By: ${event.target.textContent}`;
        });
    });

    searchButton.addEventListener("click", function() {
        const query = searchInput.value;
        fetch(`/search?query=${encodeURIComponent(query)}&type=${encodeURIComponent(searchType)}`)
            .then(response => response.json())
            .then(data => {
                const resultsContainer = document.getElementById("results");
                resultsContainer.innerHTML = data.results.map(result => `
                    <div class="result-item">
                        <p><span class="field-label">Name:</span> <span class="field-value">${result.name}</span></p>
                        <p><span class="field-label">Family:</span> <span class="field-value">${result.family}</span></p>
                        <p><span class="field-label">Year:</span> <span class="field-value">${result.year}</span></p>
                        <p><span class="field-label">Major:</span> <span class="field-value">${result.major}</span></p>
                        <p><span class="field-label">Minor:</span> <span class="field-value">${result.minor}</span></p>
                        <p><span class="field-label">LinkedIn:</span> <span class="field-value">${result.linkedin}</span></p>

                    </div>
                `).join('');
            })
            .catch(error => console.error('Error:', error));
    });
});
