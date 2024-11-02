function createAutoSlider(sliderId, wait = 3, y = false) {
  const slider = document.getElementById(sliderId);
  if (slider.children.length > 1) {
    const num = slider.children.length;

    var scrollConst = slider.children[0].offsetWidth;

    var scrolled = 0;
    var scrollVal = 0;

    var animator;
    function launchInterval() {
      animator = setInterval(function () {
        // the scroll const is being updated for everyframe, incase of a window size event
        scrollConst = y
          ? slider.children[0].offsetHeight
          : slider.children[0].offsetWidth;

        scrollVal = scrollConst * scrolled;

        slider.scrollTo({
          left: y ? 0 : scrollVal,
          top: y ? scrollVal : 0,
          behavior: "smooth",
        });

        scrolled += 1;

        if (scrolled == num) {
          scrolled = 0;
        }
      }, wait * 1000);
    }

    launchInterval();
    //////////////////

    // events to stop the animations
    slider.addEventListener("mouseenter", function (e) {
      clearInterval(animator);
    });

    slider.addEventListener("touchstart", function (e) {
      clearInterval(animator);
    });

    // events to start the animation
    slider.addEventListener("mouseleave", function (e) {
      launchInterval();
    });

    slider.addEventListener("touchend", function (e) {
      launchInterval();
    });
  }
}

function createAutoSliders(sliderIds) {
  for (const _ of sliderIds) {
    createAutoSlider(_);
  }
}
