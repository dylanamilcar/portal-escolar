function mostrarMensaje() {
    alert(
        "Aquí colocaremos próximamente toda la información para aspirantes."
    );
}

// INTRO DE ENTRADA
setTimeout(function () {
    const intro = document.getElementById("intro-video");

    if (intro) {
        intro.classList.add("intro-oculta");
    }
}, 3000);


// =========================================
// BUZÓN FLOTANTE AL HACER SCROLL
// =========================================

const buzonOriginal = document.querySelector('a[href="/buzon"]');

if (buzonOriginal) {

    const buzonFlotante = document.createElement("a");

    buzonFlotante.href = "/buzon";
    buzonFlotante.className = "buzon-flotante";
    buzonFlotante.innerHTML = "📬 Buzón";

    document.body.appendChild(buzonFlotante);

    window.addEventListener("scroll", function () {

        if (window.scrollY > 250) {
            buzonFlotante.classList.add("buzon-visible");
        } else {
            buzonFlotante.classList.remove("buzon-visible");
        }

    });
}