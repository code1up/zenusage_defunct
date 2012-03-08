Ext.define("App.profile.Tablet", {
    extend: "Ext.app.Profile",

    config: {
        views: [
            "App.view.tablet.Container",
            "App.view.Navigator",
            "App.view.account.List",
            "App.view.service.List",
            "App.view.service.Container",
            "App.view.service.About",
            "App.view.service.History",
            "App.view.service.Live"
        ],

        controllers: [
            "Tablet",
            "Navigator"
        ]
    },

    isActive: function() {
        // NOTE: make sure we have a fallback profile
        return Ext.os.is.Tablet || true;
    },

    launch: function() {
        Ext.create("App.view.tablet.Container");
    }
});
