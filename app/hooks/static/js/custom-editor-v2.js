
//** **//
//** On Page Load **//
//** **//
(function () {
    document.addEventListener('DOMContentLoaded', function () {
        // Init cusom collapsible blocks
        // IMPORTANT: DEFAULT WAGTAIL JS IS RUNNING ON INIT SO NOT NECESSARY WITH OWN CODE
        // initCustomCollapsibleBlocks();
    })
})();


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
                            // before adding clicklistener unbind old listener
                                // this is important when we change order of blocks in admin panel because this is observed as new elements added
                            $li.find('> .title-wrapper').unbind('click').on('click', function () {
                                if (!$li.hasClass('collapsed')) {
                                    $li.addClass('collapsed');
                                    $fieldset.hide('slow');
                                } else {
                                    $li.removeClass('collapsed');
                                    $fieldset.show('show');
                                }
                            });
                        });

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


//** **//
//** Collapse and add click listener to collapsible stream blocks**//
//** **//
// const initCustomCollapsibleBlocks = () => {
//     $('.object.multi-field.collapsible').each(function () {
//         var $li = $(this);
//         var $fieldset = $li.find('fieldset');
//         if ($li.hasClass('collapsed') && $li.find('.error-message').length == 0) {
//             $fieldset.hide();
//         }

//         $li.find('> .title-wrapper').on('click', function () {
//             if (!$li.hasClass('collapsed')) {
//                 $li.addClass('collapsed');
//                 $fieldset.hide('slow');
//             } else {
//                 $li.removeClass('collapsed');
//                 $fieldset.show('show');
//             }
//         });
//     });
// }
