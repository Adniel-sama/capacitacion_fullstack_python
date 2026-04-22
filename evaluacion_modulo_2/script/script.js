$(function () {
  /* ---------------- formulario contacto ---------------- */
  $('#contactForm').on('submit', function (e) {
    e.preventDefault();

    // Validación simple
    const name = $('#name').val()?.trim();
    const email = $('#email').val()?.trim();
    const message = $('#message').val()?.trim();

    function isEmail(v) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
    }

    let valid = true;
    if (!name) { valid = false; $('#name').addClass('is-invalid'); } else { $('#name').removeClass('is-invalid').addClass('is-valid'); }
    if (!isEmail(email)) { valid = false; $('#email').addClass('is-invalid'); } else { $('#email').removeClass('is-invalid').addClass('is-valid'); }
    if (!message) { valid = false; $('#message').addClass('is-invalid'); } else { $('#message').removeClass('is-invalid').addClass('is-valid'); }

    if (!valid) {
      $('#contactResult').text('Corrige los campos en rojo.').addClass('text-danger').removeClass('text-success');
      return;
    }

    // Simula envío 
    $('#contactResult').text('Mensaje enviado. Gracias.').addClass('text-success').removeClass('text-danger');
    // limpiar formulario
    setTimeout(() => {
      $('#contactForm')[0].reset();
      $('#contactForm .form-control').removeClass('is-valid');
      $('#contactResult').fadeOut(800, function(){ $(this).text('').show().removeClass('text-success'); });
    }, 1500);
  });

  /* ------- Test Modal: calcular puntaje y feedback ----- */
  $('#test').on('submit', function (e) {
    e.preventDefault();

    // Respuestas "correctas" indican prácticas seguras.
    const answers = {
      q1: 'yes', // contraseñas únicas
      q2: 'yes', // 2FA
      q3: 'yes', // backups
      q4: 'no',  // no abrir adjuntos desconocidos
      q5: 'yes'  // actualizaciones
    };

    let score = 0;
    for (let q in answers) {
      const selected = $(`[name=${q}]:checked`).val();
      if (selected === answers[q]) score++;
    }

    const percent = (score / Object.keys(answers).length) * 100;
    let feedback = '';

    if (percent === 100) {
      feedback = 'Excelente — tus prácticas básicas son seguras.';
    } else if (percent >= 60) {
      feedback = 'Bien — tienes buenas prácticas, pero puedes mejorar.';
    } else {
      feedback = 'Precaución — revisa y mejora tus prácticas.';
    }

    $('#testResult').html(`<div class="alert alert-info">Resultado: ${score}/5 — ${feedback}</div>`);
    // Cierra modal
    const modalEl = document.getElementById('testModal');
    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) modal.hide();
  });

  /* -----Tarjeta------------ */
 
  $('.card[data-bs-toggle="collapse"]').on('click', function () {
    const target = $(this).data('bs-target');
    $(target).collapse('toggle');
  });
});
