const IMG_TEMPLATE = document.getElementById("item_image_template").innerHTML;

var img_id = 0;
var all_files = new DataTransfer();

function addImages(inpt, to, func = null, func2 = null) {
  const addTo = document.getElementById(to);

  for (const file of inpt.files) {
    var img_str = IMG_TEMPLATE;

    const current_id = `img_${img_id}`;
    const img_src = URL.createObjectURL(file);

    img_str = replace_tokens(img_str, [
      ['src=""', `src='${img_src}'`],
      ["INPT_IMG_ID", current_id],
    ]);

    const obj = make_obj(img_str);
    addTo.appendChild(obj);

    obj.addEventListener("load", () => {
      URL.revokeObjectURL(img_src); // Free memory
    });

    img_id++;

    all_files.items.add(file);

    if (func) {
      func(img_src);
    }
  }

  if (func2) {
    func2();
  }

  inpt.files = all_files.files;
  //console.log(inpt.files.length);
}

function clearImages(cnt, inpt) {
  document.getElementById(cnt).innerHTML = "";
  document.getElementById(inpt).value = "";

  all_files = new DataTransfer();
}
