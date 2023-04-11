<script>
const searchWrapper = document.querySelector(".search-container");
const closeBtn = document.querySelector(".fa-times");

searchWrapper.addEventListener("click", () => {
    searchWrapper.classList.add("active");
});
closeBtn.addEventListener("click", (event) => {
    event.stopPropagation();
    searchWrapper.classList.remove("active");
});
</script>