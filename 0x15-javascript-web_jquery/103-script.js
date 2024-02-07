$(function () {
  $('INPUT#btn_translate, INPUT#language_code').on('click keypress', (_) => {
    if (_.type === 'click' || _.which === 13) {
      $
        .get('https://hellosalut.stefanbohacek.dev/',
          {lang: $('INPUT#language_code').val()},
          data => {
            $('DIV#hello').html(data.hello);
          }
      );
    }
  });
});
