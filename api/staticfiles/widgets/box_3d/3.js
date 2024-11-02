const SENSITIVITY = 2;
const DELAY = 80;

class Mode360 {
  constructor(box_id, load_anim = true) {
    this.box3d = document.getElementById(box_id);

    this.imgs = Array.from(this.box3d.children);
    this.loading_anim = null;
    if (load_anim) {
      this.loading_anim = this.imgs.pop();
    }

    this.current_indx = 0;

    this.show_angle(0);
    this.track_events_desktop();
    this.track_events_mobile();
  }

  reinit() {
    this.imgs = Array.from(this.box3d.children);
    if (this.loading_anim) {
      this.loading_anim = this.imgs.pop();
    }

    this.current_indx = 0;

    this.show_angle(0);
  }

  show_angle(indx) {    

    if (this.imgs.length) {
      this.current_indx = indx;

      // keep the index normalized
      const MAX = this.imgs.length - 1;
      if (this.current_indx > MAX) {
        this.current_indx = 0;
      }
      if (this.current_indx < 0) {
        this.current_indx = MAX;
      }

      //
      for (const img of this.imgs) {
        img.style.display = "none";
      }
      this.imgs[this.current_indx].style.display = "block";
    }
  }

  step_rotate(clockwise = true) {
    const a = clockwise ? -1 : 1;

    this.show_angle(this.current_indx + a);
  }

  track_events_desktop() {
    var focus = false;
    var lastX;
    var tick;
    const self = this;

    // detect the x1 and y1
    // get the x2 and y2 to calculate the offset

    //start the focus after the click
    this.box3d.addEventListener("mousedown", function (e) {
      focus = true;

      lastX = null;
      tick = 0;
    });

    //leave the focus after the unclick
    this.box3d.addEventListener("mouseup", function (e) {
      focus = false;
    });

    // if it is clicked and the mouse is moving OUTSIDE the box, don't move a thing
    this.box3d.addEventListener("mouseleave", function (e) {
      focus = false;
    });

    // if it is clicked and the mouse is moving INSIDE the box, move the obj
    this.box3d.addEventListener("mousemove", function (e) {
      if (focus) {
        const x = e.pageX - this.getBoundingClientRect().left;

        if (lastX == null) {
          lastX = x;
        }

        const off = lastX - x; // moving offset
        tick += off;

        if (Math.abs(tick) > SENSITIVITY) {
          const a = Math.abs(tick) / tick;

          self.step_rotate(a > 0);

          tick = 0;
        }

        lastX = x;
      }
    });
  }

  // its the excat function we just change the events
  track_events_mobile() {
    var focus = false;
    var lastX;
    var tick;
    const self = this;

    // detect the x1 and y1
    // get the x2 and y2 to calculate the offset

    //start the focus after the click
    this.box3d.addEventListener("touchstart", function (e) {
      focus = true;

      lastX = null;
      tick = 0;
    });

    //leave the focus after the unclick
    this.box3d.addEventListener("touchend", function (e) {
      focus = false;
    });

    // if it is clicked and the mouse is moving OUTSIDE the box, don't move a thing
    this.box3d.addEventListener("mouseleave", function (e) {
      focus = false;
    });

    // if it is clicked and the mouse is moving INSIDE the box, move the obj
    this.box3d.addEventListener("touchmove", function (e) {
      if (focus) {
        const x = e.touches[0].pageX - this.getBoundingClientRect().left;

        if (lastX == null) {
          lastX = x;
        }

        const off = lastX - x; // moving offset
        tick += off;

        if (Math.abs(tick) > SENSITIVITY) {
          const a = Math.abs(tick) / tick;

          self.step_rotate(a > 0);

          tick = 0;
        }

        lastX = x;
      }
    });
  }

  auto_rotate(n = -1, endFunc = null) {
    const self = this;
    var remain = n * this.imgs.length;

    const func = setInterval(function () {
      self.step_rotate();
      remain--;

      if (!remain) {
        if (endFunc) {
          endFunc();
        }
        clearInterval(func);
      }
    }, DELAY);
  }

  load_model(infinte = false) {
    const self = this;
    this.auto_rotate(3, function () {
      self.loading_anim.style.display = "none";
    });
    if (infinte) self.auto_rotate();
  }
}
