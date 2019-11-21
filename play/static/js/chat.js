$(document).ready(function(){
  $('ChatForm').submit(function(event){
    event.preventDefault()
    form = $("ChatForm")

    $.ajax({
      'url':'/ajax/message/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
    $('#id_your_message').val('')
  }) // End of submit event

}) // End of document ready function