class Cards {
  constructor(str_lst) {
    /*
    for (const ltr of ["[", "]"]) {
      str_lst = str_lst.replace(ltr, "");
    }

    const lst = str_lst.match(/datetime\.datetime\((.*?)\)/g);

    this.cards = lst.reduce((obj, key, index) => {      
      obj[key] = false;
      return obj;
    }, {});

    

    console.log(this.cards);
    */
    this.cards = {};
  }

  add_card(id) {
    this.cards[id] = false;
  }

  set_cards() {
    for (const card in this.cards) {
      const widget = document.getElementById(card);

      var arg1 = "gradient";
      var arg2 = "border";

      if (this.card_selected(card)) {
        const tmp = arg1;

        arg1 = arg2;
        arg2 = tmp;
      }

      widget.classList.replace(arg1, arg2);
    }
  }

  toggle_card(id, func) {
    const new_val = !this.cards[id];

    if (!this.at_least2() && !new_val) {
      return;
    }



    // set all to false
    for (const key of Object.keys(this.cards)){
      this.cards[key] = false
    }
    //


    this.cards[id] = new_val;
    this.set_cards();

    if (func){
      func(id);
    }
  }

  card_selected(id) {
    return this.cards[id];
  }

  set_first(func) {
    const key = Object.keys(this.cards)[0];
    this.toggle_card(key, func)
  }

  at_least2() {
    var count = 0;
    for (const key of Object.keys(this.cards)) {
      count += this.cards[key] ? 1 : 0;

      if (count > 1) {
        return true;
      }
    }
    return false;
  }
}
