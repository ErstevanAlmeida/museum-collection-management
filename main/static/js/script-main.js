async function getCollection() {
    return fetch("/get-collection/").then((res) => res.json())
}

async function refreshCollection() {
    document.getElementById("collection-card").innerHTML = ""
    const collections = await getCollection()
    collections.forEach((collection) => {
        const collectionDiv = document.createElement("div");
        collectionDiv.className = "collection collection" + collection.pk;

        const collectionCardDiv = document.createElement("div");
        collectionCardDiv.className = "collection-card";
        collectionCardDiv.addEventListener('click', function() {
            collectionCardDiv.classList.toggle('flipped');
        });

        const collectionFrontDiv = document.createElement("div");
        collectionFrontDiv.className = "collection-front";

        const collectionNameDiv = document.createElement("div");
        collectionNameDiv.className = "collection-name";

        const nameParagraph = document.createElement("p");
        nameParagraph.textContent = collection.fields.collection;
        collectionNameDiv.appendChild(nameParagraph);

        const typeParagraph = document.createElement("p");
        typeParagraph.textContent = "Type: " + collection.fields.type;

        const amountParagraph = document.createElement("p");
        amountParagraph.textContent = "Amount: " + collection.fields.amount;

        const yearParagraph = document.createElement("p");
        yearParagraph.textContent = "Year Invented: " + collection.fields.year;

        collectionFrontDiv.appendChild(collectionNameDiv);
        collectionFrontDiv.appendChild(typeParagraph);
        collectionFrontDiv.appendChild(amountParagraph);
        collectionFrontDiv.appendChild(yearParagraph);

        const collectionBackDiv = document.createElement("div");
        collectionBackDiv.className = "collection-back";

        const descriptionParagraph = document.createElement("p");
        descriptionParagraph.textContent = collection.fields.description;

        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.addEventListener("click", function() {
            window.location.href = window.editCollectionUrl;
        });

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.addEventListener("click", function() {
            window.location.href = window.deleteCollectionUrl;
        });

        collectionBackDiv.appendChild(descriptionParagraph);
        collectionBackDiv.appendChild(editButton);
        collectionBackDiv.appendChild(deleteButton);

        collectionCardDiv.appendChild(collectionFrontDiv);
        collectionCardDiv.appendChild(collectionBackDiv);

        collectionDiv.appendChild(collectionCardDiv);
        document.getElementById("collection-card").appendChild(collectionDiv);
    });
}

refreshCollection()

function addCollection() {
    fetch("/create-new-collection-ajax/", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshCollection)

    document.getElementById("form").reset()
    return false
}

function openModal() {
    modal.style.display = "block";
}

function closeModal() {
    modal.style.display = "none";
}

// Event listener untuk membuka modal saat button "Add Collection" ditekan
document.getElementById("openModalBtn").addEventListener("click", openModal);

// Event listener untuk menutup modal saat tombol "Close" di dalam modal ditekan
document.getElementById("closeModalBtn").addEventListener("click", closeModal);

// Event listener untuk menutup modal saat tombol "Add Product" di dalam modal ditekan
document.getElementById("button-add").addEventListener("click", function() {
    closeModal(); // Menutup modal
    addCollection(); // Memanggil fungsi addCollection
});