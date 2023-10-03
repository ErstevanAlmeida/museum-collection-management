document.querySelectorAll('.collection-card').forEach(function(card) {
    card.addEventListener(('click'), function() {
        card.classList.toggle('flipped');
    });
});