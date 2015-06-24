/**
 * Created by cosme.cardoso on 29/04/2015.
 */
(Function ($) {

  RemoveTableRow = function (manipulador) {
    var tr = $ (manipulador) .closest ('tr');

    tr.fadeOut (400, function () {
      tr.remove ();
    });

    return false;
  };
}) (JQuery);