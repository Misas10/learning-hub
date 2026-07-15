/* ============================================================
   Reusable quiz + recall widgets for the System Design course.
   Linked by every lesson. No lesson should inline quiz logic.

   Markup contract:

   <div class="quiz" data-answer="1" data-explain="Because ...">
     <div class="q">Question text?</div>
     <button class="opt">First option</button>
     <button class="opt">Second option</button>   <!-- index 1 = correct -->
     <button class="opt">Third option</button>
     <div class="feedback"></div>
   </div>

   - data-answer : zero-based index of the correct .opt button.
   - data-explain: feedback shown after any answer (the "why").
   Immediate, automatic feedback = the tight loop we want.
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.quiz').forEach(function (quiz) {
    var correct = parseInt(quiz.getAttribute('data-answer'), 10);
    var explain = quiz.getAttribute('data-explain') || '';
    var opts = Array.prototype.slice.call(quiz.querySelectorAll('.opt'));
    var feedback = quiz.querySelector('.feedback');

    opts.forEach(function (opt, i) {
      opt.addEventListener('click', function () {
        if (quiz.dataset.answered) return;          // lock after first try
        quiz.dataset.answered = 'true';

        opts.forEach(function (o, j) {
          o.disabled = true;
          if (j === correct) o.classList.add('correct');
        });
        if (i !== correct) opt.classList.add('wrong');

        if (feedback) {
          feedback.classList.add('show');
          feedback.innerHTML =
            (i === correct ? '✓ Correct. ' : '✗ Not quite. ') + explain;
        }
      });
    });
  });
});
