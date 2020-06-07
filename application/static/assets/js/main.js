$(document).ready(function () {
  // Content is hidden by default
  $(".collapse")
    // When the collapsible recipe element is about to be shown change the plus icon into minus icon
    .on("show.bs.collapse", function () {
      $(this)
        .prev(".card-header")
        .find(".fa-plus")
        .removeClass("fa-plus")
        .addClass("fa-minus");
    })
    // When the collapsible recipe element is about to be hidden change the minus icon into plus icon
    .on("hide.bs.collapse", function () {
      $(this)
        .prev(".card-header")
        .find(".fa-minus")
        .removeClass("fa-minus")
        .addClass("fa-plus");
    });
});
