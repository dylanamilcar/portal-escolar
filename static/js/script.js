document.addEventListener('DOMContentLoaded', () => {
    const intro = document.getElementById('intro-video');
    if (intro) {
        setTimeout(() => {
    intro.classList.add("oculto");
}, 700);
    }

    const board = document.getElementById('buzon-board');
    if (board) board.scrollTop = board.scrollHeight;

    const notification = document.getElementById('buzon-notificacion');
    if (notification) {
        const lastSeen = Number(localStorage.getItem('buzonUltimoVisto') || 0);
        const current = Number(document.body.dataset.ultimoMensaje || 0);
        if (current > lastSeen) notification.textContent = ' NUEVO';
        document.querySelectorAll('a[href$="/buzon"]').forEach(link => {
            link.addEventListener('click', () => localStorage.setItem('buzonUltimoVisto', String(current)));
        });
    }
});
