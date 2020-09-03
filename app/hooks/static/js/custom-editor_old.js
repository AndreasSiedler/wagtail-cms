// Detect new added Nodes
(function () {

    document.addEventListener('DOMContentLoaded', function () {
  
  
      // Select the node that will be observed for mutations
      const targetNode = document.getElementById('body-list');
  
      targetNode.querySelectorAll('.block_setting_choice select').forEach(function (el) {
        console.log(el);
        el.addEventListener('change', function (el) {
          console.log(el.target.value)
  
          var choice_handler_value = el.target.value
          var parent_block = el.target.closest('.c-sf-block');
  
          parent_block.querySelectorAll('.block_settings_field.show_if').forEach(function (el) {
            el.parentElement.style.display = 'none';
          });
    
          parent_block.querySelectorAll(`.block_settings_field.show_if.${choice_handler_value}`).forEach(function (el) {
            el.parentElement.style.display = 'block';
          });
        })
      });
  
      // Options for the observer (which mutations to observe)
      const config = { attributes: true, childList: true, subtree: true };
  
      // Callback function to execute when mutations are observed
      const callback = function (mutationsList, observer) {
        // Use traditional 'for loops' for IE 11
        for (let mutation of mutationsList) {
          if (mutation.type === 'attributes') {
  
          }
          if (mutation.type === 'childList') {
            console.log('A child node has been added or removed.');
            mutation.addedNodes.forEach(function (container) {
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
    var selector = '.block_settings_field.select';
  
    document.addEventListener('click', function (e) {
  
      var el = e.target;
      var el_parent = el.closest(selector);
  
      if (!el_parent) {
        return;
      }
  
      el.addEventListener('change', function (el) {
        console.log(el.target.value)
        var choice_handler_value = el.target.value
        var parent_block = el_parent.closest('.c-sf-block');
  
        parent_block.querySelectorAll('.block_settings_field.show_if').forEach(function (el) {
          el.parentElement.style.display = 'none';
        });
  
        parent_block.querySelectorAll(`.block_settings_field.show_if.${choice_handler_value}`).forEach(function (el) {
          el.parentElement.style.display = 'block';
        });
      }, { once: true })
  
    })
  })();
  
  
  // DomContentLoaded
  (function () {
    document.addEventListener('DOMContentLoaded', function () {
      var settings_active = false;
      var container_list = document.getElementById('body-list');
      // console.log(container_list);
  
      // container_list.querySelectorAll('.wagtailuiplus__choice-handler select').forEach(function(el) {
      //   show_hide_elements(el, el.value);
      // });
      // container_list.forEach(function(container) {
      //   console.log(container);
      //   add_setting_icon_to_container(container);
      //   hide_setting_fields(container);
      // })
  
      // Add Setting Icons
      container_list.querySelectorAll('.c-sf-block__actions').forEach(function (node) {
        add_setting_icon(node);
        // hide_setting_fields(el);
      })
  
      // Hide all setting fields
      container_list.querySelectorAll('.block_settings_field').forEach(function (node) {
        hide_field_from_class(node);
        // hide_setting_fields(el);
      })
  
  
    });
  })();
  
  
  // Helperfunctions
  const add_setting_icon = (node) => {
    var button = document.createElement("button");        // Create setting button
    button.setAttribute('class', 'c-sf-block__actions__single block-settings-button')
    button.innerHTML = '<i class="icon icon-cog" aria-hidden="true"></i>';
    button.onclick = function (e) {
      e.preventDefault();
      toggle_all_unconditional_fields(node);
    }
    node.appendChild(button);
  }
  
  const hide_field_from_class = (node) => {
    node.parentElement.style.display = 'none';
  }
  
  const toggle_all_unconditional_fields = (node) => {
    var parent_block = node.closest('.c-sf-block')
    parent_block.querySelectorAll('.field > .field:not(.show_if)').forEach(function (el) {
      if (el.parentElement.style.display === "none") {
        el.parentElement.style.display = "block";
      } else {
        el.parentElement.style.display = "none";
      };
    });
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  const show_hide_elements = (el, value) => {
    var parent_block = el.closest('.c-sf-block');
  
    parent_block.querySelectorAll('.wagtailuiplus__show_if').forEach(function (el) {
      el.parentElement.style.display = 'none';
    });
  
    parent_block.querySelectorAll(`.wagtailuiplus__show_if.${value}`).forEach(function (el) {
      el.parentElement.style.display = 'block';
    });
  }
  
  const hide_setting_fields = (node) => {
    var parent_block = node.closest('.c-sf-block')
    parent_block.querySelectorAll('.wagtailuiplus__show_if.setting').forEach(function (el) {
      el.style.display = "none";
    });
  }
  
  
  
  // Detect new added Nodes
  (function () {
  
    document.addEventListener('DOMContentLoaded', function () {
  
      // Select the node that will be observed for mutations
      const targetNode = document.getElementById('body-list');
      console.log(targetNode);
  
      // Options for the observer (which mutations to observe)
      const config = { attributes: true, childList: true, subtree: true };
  
      // Callback function to execute when mutations are observed
      const callback = function (mutationsList, observer) {
        // Use traditional 'for loops' for IE 11
        for (let mutation of mutationsList) {
          if (mutation.type === 'childList') {
            console.log('A child node has been added or removed.');
            mutation.addedNodes.forEach(function (container) {
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