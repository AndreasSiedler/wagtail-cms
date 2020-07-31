

// var x = document.getElementsByClassName("example");
// console.log(x);
// Event handler for choice blocks with conditional visibility
function onChoiceHandlerChange(target) {
    const choiceHandler = target.closest('.wagtailuiplus__choice-handler');
    if (choiceHandler !== null) {
      let choiceHandlerValue;
      if (choiceHandler.classList.contains('boolean_field')) {
        choiceHandlerValue = choiceHandler.querySelector('input[type=checkbox]').checked ? 'true' : 'false';
      } else {
        choiceHandlerValue = choiceHandler.querySelector('select').value;
      }
  
      let searchContainer;
      // If the chocie handler is a char field or boolean field, search in the entire edit form
      if (choiceHandler.classList.contains('typed_choice_field') || choiceHandler.classList.contains('boolean_field')) {
        searchContainer = choiceHandler.closest('form');
      // Otherwise, if the choice handler is a choices block, search in the entire struct block
      } else {
         searchContainer = choiceHandler.closest('ul.fields');
      }
  
      const choiceHandlerIdRegex = /wagtailuiplus__choice-handler--([a-zA-Z\-\_\d]+)/;
      const choiceHandlerId = choiceHandlerIdRegex.exec(choiceHandler.className)[1];
      const choiceHandlerTargets = searchContainer.querySelectorAll('.wagtailuiplus__choice-handler-target--' + choiceHandlerId);
      const hiddenIfRegex = /wagtailuiplus__choice-handler-hidden-if--([a-zA-Z\-\_\d]+)/g;
      let hiddenIfValue;
      let matches;
      let hiddenIfs;
      let hiddenIfIndex;
      for (let j = 0; j < choiceHandlerTargets.length; j++) {
        matches = hiddenIfRegex.exec(choiceHandlerTargets[j].className);
        while (matches !== null) {
          hiddenIfValue = matches[1];
          choiceHandlerTargetContainer = choiceHandlerTargets[j].closest('li');
          if (choiceHandlerValue === hiddenIfValue) {
            if (choiceHandlerTargetContainer.hasAttribute('data-wagtailuiplus-hidden-ifs')) {
              hiddenIfs = choiceHandlerTargetContainer.getAttribute('data-wagtailuiplus-hidden-ifs').split(',');
              if (!hiddenIfs.includes(hiddenIfValue)) {
                hiddenIfs.push(hiddenIfValue);
              }
              choiceHandlerTargetContainer.setAttribute('data-wagtailuiplus-hidden-ifs', hiddenIfs.join(','));
            } else {
              choiceHandlerTargetContainer.setAttribute('data-wagtailuiplus-hidden-ifs', hiddenIfValue);
            }
            if (!choiceHandlerTargetContainer.classList.contains('wagtailuiplus__choice-handler-target--hidden')) {
              choiceHandlerTargetContainer.classList.add('wagtailuiplus__choice-handler-target--hidden');
            }
          } else if (choiceHandlerTargetContainer.hasAttribute('data-wagtailuiplus-hidden-ifs')) {
            hiddenIfs = choiceHandlerTargetContainer.getAttribute('data-wagtailuiplus-hidden-ifs').split(',');
            hiddenIfIndex = hiddenIfs.indexOf(hiddenIfValue);
            if (hiddenIfIndex > -1) {
              hiddenIfs.splice(hiddenIfIndex, 1);
              if (hiddenIfs.length === 0) {
                choiceHandlerTargetContainer.classList.remove('wagtailuiplus__choice-handler-target--hidden');
                choiceHandlerTargetContainer.removeAttribute('data-wagtailuiplus-hidden-ifs');
              } else {
                choiceHandlerTargetContainer.setAttribute('data-wagtailuiplus-hidden-ifs', hiddenIfs.join(','));
              }
            }
          }
          matches = hiddenIfRegex.exec(choiceHandlerTargets[j].className);
        }
      }
    }
  }  


// Initialize a choice handler
function initChoiceHandler(structBlockContainer) {
    structBlockContainer.addEventListener('change', function(event) {
      onChoiceHandlerChange(event.target);
    });
}


// Initialize all event handlers on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log("Hallo");
    let i;

    // Initialize choice handler for selectboxes not contained in stream fields
    const choiceHandlersCharFieldSelects = document.getElementsByClassName('field');
    console.log(choiceHandlersCharFieldSelects);

    for (i = 0; i < choiceHandlersCharFieldSelects.length; i++) {
        initChoiceHandler(choiceHandlersCharFieldSelects[i]);
        onChoiceHandlerChange(choiceHandlersCharFieldSelects[i]);
    }
});