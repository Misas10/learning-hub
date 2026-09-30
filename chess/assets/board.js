/* ============================================================
   Reusable static chess diagram for the Chess course.
   Linked by every lesson that shows a position. No lesson
   should hand-draw a board.

   Markup contract:

   <div class="board"
        data-fen="4r1k1/pp3ppp/4q3/8/8/1QN5/PP3PPP/3R2K1 w - - 0 1"
        data-marks="b3 e6"></div>

   - data-fen  : position in FEN (only the piece-placement field is
                 read; the rest may be present or omitted).
   - data-marks: optional space-separated squares to outline.
   Always drawn from White's side (a1 bottom-left), matching the
   glossary's convention.
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {
  var GLYPH = { k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟' };
  var FILES = 'abcdefgh';

  document.querySelectorAll('.board').forEach(function (el) {
    var rows = (el.getAttribute('data-fen') || '').split(' ')[0].split('/');
    var marks = (el.getAttribute('data-marks') || '').split(/\s+/);
    var html = '';

    rows.forEach(function (row, r) {
      var rank = 8 - r;
      var f = 0;
      html += '<div class="coord">' + rank + '</div>';
      row.split('').forEach(function (ch) {
        var n = parseInt(ch, 10);
        var count = isNaN(n) ? 1 : n;
        for (var i = 0; i < count; i++) {
          var name = FILES[f] + rank;
          var cls = 'sq ' + ((f + rank) % 2 === 0 ? 'light' : 'dark');
          if (marks.indexOf(name) !== -1) cls += ' mark';
          var glyph = '';
          if (isNaN(n)) {
            cls += ch === ch.toUpperCase() ? ' w' : ' b';
            glyph = GLYPH[ch.toLowerCase()];
          }
          html += '<div class="' + cls + '" title="' + name + '">' + glyph + '</div>';
          f++;
        }
      });
    });

    html += '<div class="coord"></div>';
    FILES.split('').forEach(function (c) { html += '<div class="coord">' + c + '</div>'; });
    el.innerHTML = html;
  });
});
