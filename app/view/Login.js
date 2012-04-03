(function() {
    var loginButton = Ext.create("Ext.Button", {
        id: "loginButton",
        ui: "confirm",
        text: "Login"
    });

    var cancelButton = Ext.create("Ext.Button", {
        id: "cancelButton",
        ui: "decline",
        text: "Cancel"
    });

    Ext.define("App.view.Login", {
        extend: "Ext.Panel",
        xtype: "login",

        config: {
            layout: "vbox",

            items: [
                loginButton,
                cancelButton
            ]
        }
    });
})();
