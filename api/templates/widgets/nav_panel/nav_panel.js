class NavPanel {
  constructor(urls, box="nav_cards") {
    this.urls = urls;
    this.box = box
  }

  set_select() {
    const CARDS = document.getElementById(this.box).children;

    for (var i = this.urls.length; i > 0; i--) {
      const token = this.urls[i - 1];
      if (window.location.pathname.includes(token)) {
        const widget = CARDS[i- 1 ]
        widget.classList.add("selected")
        break;
      }
    }
  }
}
