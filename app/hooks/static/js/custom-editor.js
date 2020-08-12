// Helperfunctions
const show_hide_elements = (el, value) => {
  var parent_block = el.closest('.c-sf-block');

  parent_block.querySelectorAll('.wagtailuiplus__show_if').forEach(function(el){
    el.parentElement.style.display = 'none';
  });

  parent_block.querySelectorAll(`.wagtailuiplus__show_if.${value}`).forEach(function(el){
    el.parentElement.style.display = 'block';
  });
}

// DomContentLoaded
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var container_list = document.getElementById('content-list');
    console.log(container_list.querySelectorAll('.wagtailuiplus__choice-handler select'));
    container_list.querySelectorAll('.wagtailuiplus__choice-handler select').forEach(function(el) {
      show_hide_elements(el, el.value);
    });
  });
})();

// Detect new added Nodes
(function() {

  document.addEventListener('DOMContentLoaded', function() {

    // Select the node that will be observed for mutations
    const targetNode = document.getElementById('content-list');

    // Options for the observer (which mutations to observe)
    const config = { attributes: false, childList: true, subtree: false };

    // Callback function to execute when mutations are observed
    const callback = function(mutationsList, observer) {
        // Use traditional 'for loops' for IE 11
        for(let mutation of mutationsList) {
            if (mutation.type === 'childList') {
                console.log('A child node has been added or removed.');
                mutation.addedNodes.forEach(function(container){
                  container.querySelectorAll('.wagtailuiplus__show_if').forEach(function (el) {
                    el.parentElement.style.display = 'none'
                  });
                })
            }
            // else if (mutation.type === 'attributes') {
            //     console.log('The ' + mutation.attributeName + ' attribute was modified.');
            // }
        }
    };

    // Create an observer instance linked to the callback function
    const observer = new MutationObserver(callback);

    // Start observing the target node for configured mutations
    observer.observe(targetNode, config);

    // Later, you can stop observing
    // observer.disconnect();

  });
})();


// Select Value is changed
(function () {
  var selector = '.wagtailuiplus__choice-handler';

  document.addEventListener('click', function (e) {

    var el = e.target;
    var el_parent = el.closest(selector);

    if (!el_parent) {
      return;
    }

    el.addEventListener('change', function (el) {
      var choice_handler_value = el.target.value
      var parent_block = el_parent.closest('.c-sf-block');

      parent_block.querySelectorAll('.wagtailuiplus__show_if').forEach(function(el){
        el.parentElement.style.display = 'none';
      });

      parent_block.querySelectorAll(`.wagtailuiplus__show_if.${choice_handler_value}`).forEach(function(el){
        el.parentElement.style.display = 'block';
      });
    }, { once: true })

  })
})();