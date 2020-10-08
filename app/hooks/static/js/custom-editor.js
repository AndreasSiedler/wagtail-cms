
//** **//
//** On Page Load **//
//** **//
(function () {
  document.addEventListener('DOMContentLoaded', function () {

    // Init cusom collapsible blocks
    initCustomCollapsibleBlocks();

    // Select the node that will be observed for mutations
    const targetNode = document.getElementById('content-list');

    //Append Setting Icons on Page Load
    targetNode.querySelectorAll('.c-sf-block__actions').forEach(function (el) {
      var button = document.createElement("button");        // Create setting button
      button.setAttribute('class', 'c-sf-block__actions__single block-settings-button');
      button.innerHTML = '<i class="icon icon-cog" aria-hidden="true"></i>';
      button.onclick = function (e) {
        e.preventDefault();
        onActivateSettings(this);
      }
      el.appendChild(button);
    })

    //Append Choice Field Click Listeners
    targetNode.querySelectorAll('.block_setting_choice, block_content_choice').forEach(function (el) {
      el.addEventListener('change', function (event) {
        onSelectChoice(el, event.target.value);
      })
    })

    // Hide all Settings on Page Load
    targetNode.querySelectorAll(".block_setting_field, .block_setting_choice, .block_setting_sub").forEach(function (el) {
      el.parentElement.style.display = 'none';
    })

    // Style Sub Fields
    targetNode.querySelectorAll(".block_setting_sub").forEach(function (el) {
      el.parentElement.style.width = '60%';
    })
  })
})();


//** **//
//** Collapse and add click listener to collapsible stream blocks**//
//** **//
const initCustomCollapsibleBlocks = () => {
  $('.object.multi-field.collapsible').each(function () {
    var $li = $(this);
    var $fieldset = $li.find('fieldset');
    if ($li.hasClass('collapsed') && $li.find('.error-message').length == 0) {
      $fieldset.hide();
    }

    $li.find('> .title-wrapper').on('click', function () {
      if (!$li.hasClass('collapsed')) {
        $li.addClass('collapsed');
        $fieldset.hide('slow');
      } else {
        $li.removeClass('collapsed');
        $fieldset.show('show');
      }
    });
  });
}


//** **//
//** On Settings Clicked **//
//** **//
const onActivateSettings = (settingsButton) => {

  //Change Button
  settingsButton.setAttribute('style', 'color: #f37e77');
  settingsButton.onclick = function (e) {
    e.preventDefault();
    onDeactivateSettings(this);
  }
  // Hide all Content fields
  var parentContainer = settingsButton.closest('.c-sf-block');
  parentContainer.querySelectorAll('.block_content_field').forEach(function (el) {
    el.parentElement.style.display = 'none';
  })
  // Show all choice and field Setting fields
  parentContainer.querySelectorAll(".block_setting_field").forEach(function (el) {
    el.parentElement.style.display = 'block';
  })
  // Show all choice and field Setting fields
  parentContainer.querySelectorAll(".block_setting_choice, block_content_choice").forEach(function (el) {
    el.parentElement.style.display = 'block';
    el.querySelectorAll("select").forEach(function (el) {

      const value = el.options[el.selectedIndex].value;
      if (value) {
        var parentContainer = el.closest('.c-sf-block');
        // Show specific sub fields
        parentContainer.querySelectorAll(`.block_setting_sub.${value}`).forEach(function (el) {
          console.log(el);
          el.parentElement.style.display = 'block';
        })
      }
    })
  })


}

const onDeactivateSettings = (settingsButton) => {

  console.log("Deactivate Settings clicked");
  //Change Button
  settingsButton.setAttribute('style', 'color: none');
  settingsButton.onclick = function (e) {
    e.preventDefault();
    onActivateSettings(this);
  }
  // Hide all Setting fields
  var parentContainer = settingsButton.closest('.c-sf-block');
  parentContainer.querySelectorAll('.block_setting_field, .block_setting_choice, .block_setting_sub').forEach(function (el) {
    el.parentElement.style.display = 'none';
  })
  // Show all Content fields
  var parentContainer = settingsButton.closest('.c-sf-block');
  parentContainer.querySelectorAll('.block_content_field').forEach(function (el) {
    el.parentElement.style.display = 'block';
  })

}


//** **//
//** On Select Coice Field **//
//** **//
const onSelectChoice = (selectField, value) => {
  var parentContainer = selectField.closest('.c-sf-block');
  console.log(`.block_setting_sub.${value}`);
  //Hide all Sub Fields
  parentContainer.querySelectorAll('.block_setting_sub').forEach(function (el) {
    el.parentElement.style.display = 'none';
  })
  // Show specific sub fields
  if (value) {
    parentContainer.querySelectorAll(`.block_setting_sub.${value}`).forEach(function (el) {
      console.log(el);
      el.parentElement.style.display = 'block';
    })
  }
}


//** **//
//** On Select Block Added **//
//** **//
(function () {

  document.addEventListener('DOMContentLoaded', function () {

    // Select the node that will be observed for mutations
    const targetNode = document.getElementById('content-list');
    // Options for the observer (which mutations to observe)
    const config = { attributes: false, childList: true, subtree: false };
    // Callback function to execute when mutations are observed
    const callback = function (mutationsList, observer) {
      // Use traditional 'for loops' for IE 11
      for (let mutation of mutationsList) {
        if (mutation.type === 'childList') {
          console.log('A child node has been added or removed.',);
          mutation.addedNodes.forEach(function (container) {

            //** **//
            //** Collapse and add click listener to collapsible stream blocks**//
            //** **//
            var $container = $(container);
            $container.find('.object.multi-field.collapsible').each(function () {
              var $li = $(this);
              var $fieldset = $li.find('fieldset');
              if ($li.hasClass('collapsed') && $li.find('.error-message').length == 0) {
                $fieldset.hide();
              }

              $li.find('> .title-wrapper').on('click', function () {
                if (!$li.hasClass('collapsed')) {
                  $li.addClass('collapsed');
                  $fieldset.hide('slow');
                } else {
                  $li.removeClass('collapsed');
                  $fieldset.show('show');
                }
              });
            });



            console.log(container);
            //Append Setting Icons on Page Load
            container.querySelectorAll('.c-sf-block__actions').forEach(function (el) {
              var button = document.createElement("button");        // Create setting button
              button.setAttribute('class', 'c-sf-block__actions__single block-settings-button');
              button.innerHTML = '<i class="icon icon-cog" aria-hidden="true"></i>';
              button.onclick = function (e) {
                e.preventDefault();
                onActivateSettings(this);
              }
              el.appendChild(button);
            })

            //Append Choice Field Click Listeners
            container.querySelectorAll('.block_setting_choice, block_content_choice').forEach(function (el) {
              el.addEventListener('change', function (event) {
                onSelectChoice(el, event.target.value);
              })
            })

            // Hide all Settings on Page Load
            container.querySelectorAll(".block_setting_field, .block_setting_choice, .block_setting_sub").forEach(function (el) {
              el.parentElement.style.display = 'none';
            })

            // Style Sub Fields
            container.querySelectorAll(".block_setting_sub").forEach(function (el) {
              el.parentElement.style.width = '60%';
            })

          })
        }
      }
    };
    const observer = new MutationObserver(callback);
    observer.observe(targetNode, config);
    // Later, you can stop observing
    // observer.disconnect();

  });
})();