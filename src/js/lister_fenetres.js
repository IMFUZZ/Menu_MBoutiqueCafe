$("body").on("click", ".retirer", function() {
    var context = ko.contextFor(this),
        id = context.$data.id();
    if (id != 0) {
      context.$data.id(-id);
    } else {
      context.$parent.zones.remove(context.$data);
    }
});

$("body").on("click", ".ajouter_fenetre", function() {
  var context = ko.contextFor(this);
  var Fenetre = function(){
    this.id = ko.observable(0);
    this.nom = ko.observable($("#nom_fenetre_input").val());
    this.theme = ko.observable(context.$root.themes()[0]);
    this.zones = ko.observableArray([]);
  };

  context.$root.fenetres.push(new Fenetre());
});

$("body").on("click", ".ajouter_zone", function() {
  var context = ko.contextFor(this);
  console.log(context);
  var Zone = function(){
    this.id = ko.observable(0);
    this.nom = ko.observable($("#nom_zone_input").val());
    this.type = ko.observable($("#choix_type_zone").val());
  };
  
  //context.$data.zones.push(new Zone());

});

$('body').on('shown.bs.modal', '#modalAjouterFenetre', function () {
  $('#nom_fenetre_input').focus();
})

$('body').on('shown.bs.modal', '#modalAjouterZone', function () {
  $('#nom_zone_input').focus();
})