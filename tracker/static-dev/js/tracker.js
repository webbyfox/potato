$('.selectmultiple').chosen({}).change( function(obj, result) {
    console.debug("changed: %o", arguments);
    
    console.log("selected: " + result.selected);
});