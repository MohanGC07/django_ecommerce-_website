document.addEventListener("DOMContentLoaded", function () {
    const itemsPerPage = 3;
    const items = document.querySelectorAll('.col');
    const totalPages = Math.ceil(items.length / itemsPerPage);
    let currentPage = 1;

    function showPage(page) {
        const startIndex = (page - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;

        items.forEach((item, index) => {
            if (index >= startIndex && index < endIndex) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }

    function updatePagination() {
        const prevBtn = document.getElementById('prev');
        const nextBtn = document.getElementById('next');

        prevBtn.addEventListener('click', () => {
            if (currentPage > 1) {
                currentPage--;
                showPage(currentPage);
            }
        });

        nextBtn.addEventListener('click', () => {
            if (currentPage < totalPages) {
                currentPage++;
                showPage(currentPage);
            }
        });
    }

    showPage(currentPage);
    updatePagination();
});