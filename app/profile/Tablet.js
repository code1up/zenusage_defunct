Ext.define("ZenUsage.profile.Tablet", {
    extend: "Ext.app.Profile",

    config: {
        views: [
            "ZenUsage.view.AccountListView",
            "ZenUsage.view.NavigationView",
            "ZenUsage.view.ServiceAboutView",
            "ZenUsage.view.ServiceHistoryView",
            "ZenUsage.view.ServiceListView",
            "ZenUsage.view.ServiceLiveView",
            "ZenUsage.view.ServiceTabView",
            "ZenUsage.view.tablet.MainView"
        ],

        controllers: [
            "Controller"
        ]
    },

    isActive: function() {
        // NOTE: make sure we have a fallback profile
        return Ext.os.is.Tablet || true;
    },

    launch: function() {
        console.log("profile.Tablet::launch");
        Ext.create("ZenUsage.view.tablet.MainView");
    }
});
