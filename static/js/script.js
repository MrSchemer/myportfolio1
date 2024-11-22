function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-btn');
    sidebar.classList.toggle('sidebar-open');
    toggleBtn.classList.toggle('open');
    toggleBtn.textContent = sidebar.classList.contains('sidebar-open') ? '✕' : '☰';
}
