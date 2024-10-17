// image_view.js

function addText() {
    var textContent = document.getElementById("text-content").value;
    var textElement = document.createElement("p");
    textElement.innerText = textContent;
    textElement.classList.add("added-text"); // Tambahkan class untuk gaya teks yang baru ditambahkan
    document.querySelector(".image-container").appendChild(textElement);

    // Mengatur posisi teks sesuai dengan posisi kursor mouse
    var imageContainer = document.querySelector(".image-container");
    var rect = imageContainer.getBoundingClientRect();
    var mouseX = event.clientX - rect.left;
    var mouseY = event.clientY - rect.top;
    textElement.style.left = mouseX + "px";
    textElement.style.top = mouseY + "px";
}
