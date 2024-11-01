class Mode360 {
    constructor(id) {
      //consts
      this.SENSITIVITY = 2;
      this.DELAY = 80;
  
      //
      this.box3d = document.getElementById(id);
  
      this.init();
  
      //events
      this.enable_resize_event();
  
      this.track_events_desktop();
      this.track_events_mobile();
    }
  
    //special creator mode
    init() {
      const elems = Array.from(this.box3d.children);
  
      // enable the animation
      this.anim = elems.pop();
      this.anim.style.display = "flex";
  
      // init the cnv
      this.cnv = elems.pop();
      this.ctx = this.cnv.getContext("2d");
      this.cnv_init();
  
      // load the images
      this.current_indx = 0;
      this.imgs = [];
  
      Promise.all(
        Array.from(elems[0].children).map((_) => {
          return new Promise((resolve, reject) => {
            const img = new Image();
            img.src = _.src;
            _.remove();
  
            img.onload = () => resolve(img);
            img.onerror = () => reject(new Error("angle error"));
          });
        })
      ).then((imgs) => {
        this.imgs = imgs;
  
        // render the first angle
        this.draw_angle(0);
        this.load_ok();
        this.auto_rotate(2, () => {
          this.auto_rotate(-2);        
        });
      });
    }
  
    load_ok() {
      this.anim.style.display = "none";
    }
  
    // canvas
  
    cnv_init() {
      this.cnv.width = this.box3d.offsetWidth;
      this.cnv.height = this.box3d.offsetHeight;
    }
    draw_angle(indx) {
      // check the indx
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
  
        // draw
        const img = this.imgs[this.current_indx];
        this.ctx.drawImage(
          img,
          //
          0,
          0,
          img.width,
          img.height,
          //
          0,
          0,
          this.cnv.width,
          this.cnv.height
        );
      }
    }
  
    // rotate
    step_rotate(clockwise = true) {
      const a = clockwise ? -1 : 1;
  
      this.draw_angle(this.current_indx + a);
    }
  
    // events
  
    enable_resize_event() {
      window.addEventListener("resize", () => {
        this.cnv_init();
        this.draw_angle(this.current_indx);
      });
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
  
          if (Math.abs(tick) > self.SENSITIVITY) {
            const a = Math.abs(tick) / tick;
  
            self.step_rotate(a > 0);
  
            tick = 0;
          }
  
          lastX = x;
        }
      });
    }
  
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
  
          if (Math.abs(tick) > self.SENSITIVITY) {
            const a = Math.abs(tick) / tick;
  
            self.step_rotate(a > 0);
  
            tick = 0;
          }
  
          lastX = x;
        }
      });
    }
  
    // auto
    auto_rotate(n = 1, endFunc = null) {
      if (this.imgs.length) {
        const self = this;
        var remain = Math.abs(n) * this.imgs.length;
        const clk = n > 0;
  
        const func = setInterval(function () {
          self.step_rotate(clk);
          remain--;
  
          if (!remain) {
            if (endFunc) {
              endFunc();
            }
            clearInterval(func);
          }
        }, self.DELAY);
      }
    }
  }
  